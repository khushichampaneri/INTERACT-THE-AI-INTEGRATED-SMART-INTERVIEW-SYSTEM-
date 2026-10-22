from reportlab.pdfgen import canvas



def generate_report(data):


    pdf=canvas.Canvas(

    "reports/report.pdf"

    )



    y=800



    for k,v in data.items():


        pdf.drawString(

        50,
        y,

        str(k)+" : "+str(v)

        )



        y-=40



    pdf.save()