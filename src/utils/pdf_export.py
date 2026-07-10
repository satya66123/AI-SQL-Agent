from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

import io


class PDFExport:

    @staticmethod
    def create(

        question,

        database,

        query,

        explanation,

        rows,

        execution_time

    ):

        buffer = io.BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        elements = [Paragraph("<b>AI SQL AGENT REPORT</b>", styles["Heading1"]),
                    Paragraph(f"<b>Question:</b><br/>{question}", styles["BodyText"]),
                    Paragraph(f"<b>Database:</b><br/>{database}", styles["BodyText"]),
                    Paragraph(f"<b>Generated Query:</b><br/>{query}", styles["BodyText"]),
                    Paragraph(f"<b>Rows Returned:</b> {rows}", styles["BodyText"]),
                    Paragraph(f"<b>Execution Time:</b> {execution_time} sec", styles["BodyText"]),
                    Paragraph(f"<b>AI Explanation:</b><br/>{explanation}", styles["BodyText"])]

        doc.build(elements)

        buffer.seek(0)

        return buffer