import pypdfium2 as pdfium
from workspace.network_client.utils import NerStringUtils
import json
import pandas
import tabula

def performNerAnalysis(EngineInstance, boxes, PATH_TO_PDF, categoryarr, im_width, im_height):
    jsout = {}
    i = 0
    for box in boxes['detection_boxes']:
        if boxes['detection_scores'][i] > 0.3:
            print("==================================================================================")
            print(str(boxes['detection_classes'][i]))
            print("==================================================================================")
            currentitem = categoryarr[int(boxes['detection_classes'][i])]["name"]
            
            if not "(serial)" in currentitem:
                jsout[currentitem] = {}
                pdf = pdfium.PdfDocument(PATH_TO_PDF)
                im_width,im_height = pdf.get_page_size(0)
                version = pdf.get_version()  # get the PDF standard version
                n_pages = len(pdf)  # get the number of pages in the document

                page = pdf[0]

                # Load a text page helper
                textpage = page.get_textpage()
                # Extract text from the whole page
                (left, right, top, bottom) = (box[1] * im_width, box[3] * im_width,
                                    box[0] * im_height, box[2] * im_height)
                
                text_all = textpage.get_text_bounded(bottom=im_height-bottom,left=left, right=right, top=im_height-top)
                print(repr(text_all))
                print("==================================================================================")
                jsout = getresult(NerStringUtils.performStringNormalisation(text_all), EngineInstance, jsout, currentitem)
            else:
                jsout[currentitem] = []
                try:
                    tables = tabula.read_pdf(PATH_TO_PDF, area=((box[0] * im_height, box[1] * im_width, box[2] * im_height, box[3] * im_width)), pandas_options={'header': None}, pages="1")
                    vals = tables[0]
                    vals = vals.rename(columns={ 0 : "val"})
                    for index, row in vals.iterrows():
                        jsout[currentitem].append(int(row["val"]))
                except:
                    pass
            i = i + 1
    with open('workspace/network_client/output/AWB.json', 'w') as curr:
        json.dump(jsout, curr)
    
    return jsout

def getresult(text, EngineInstance, jsout, currentitem):
    textarr = text.split("\n")
    for line in textarr:
        try :
            classifcation = EngineInstance.recommendations(line, as_df=False)
            try:
                val = classifcation[classifcation["jaccard_value"] > 0.3].iloc[0]["group"]
                print(line, val)
            except:
                if len(classifcation.index) > 4 and len(classifcation['group'].unique()) == 1:
                    val = classifcation.iloc[0]["group"]
                    print(line, val)
            jsout[currentitem][val] = line
        except :
                classifcation = None
    return jsout


        