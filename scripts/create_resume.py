from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path("/home/ubuntu/curriculo-rickelme-publico.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = HexColor("#0b3b52")
BLUE = HexColor("#3f76e8")
INK = HexColor("#183b4d")
MUTED = HexColor("#54707c")
LIGHT = HexColor("#f4f8fb")

styles = getSampleStyleSheet()
name_style = ParagraphStyle("Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=NAVY, spaceAfter=4)
role_style = ParagraphStyle("Role", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, leading=14, textColor=BLUE, spaceAfter=10)
section_style = ParagraphStyle("Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=NAVY, spaceBefore=6, spaceAfter=5)
body_style = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.2, leading=13, textColor=INK, spaceAfter=4)
small_style = ParagraphStyle("Small", parent=body_style, fontSize=8.8, leading=12)
meta_style = ParagraphStyle("Meta", parent=body_style, fontSize=8.8, leading=12, textColor=MUTED)

story = []
story.append(Paragraph("Rickelme Gouveia", name_style))
story.append(Paragraph("Jovem Aprendiz em desenvolvimento | Tecnologia · Administração · Operações", role_style))
story.append(Paragraph("E-mail profissional: rickelmegouveia@gmail.com", meta_style))
story.append(Spacer(1, 5))
story.append(HRFlowable(width="100%", thickness=1.2, color=BLUE, spaceBefore=2, spaceAfter=9))

story.append(Paragraph("OBJETIVO", section_style))
story.append(Paragraph("Busco uma oportunidade como Jovem Aprendiz para desenvolver minhas habilidades profissionais, contribuir para o sucesso da empresa e adquirir experiência no ambiente de trabalho.", body_style))

story.append(Paragraph("PERFIL", section_style))
story.append(Paragraph("Estudante do ensino médio e profissional em início de carreira, com experiência prática em supermercado e interesse em rotinas administrativas, processos, tecnologia, desenvolvimento de sistemas e automação. Tenho iniciativa para aprender e utilizo ferramentas digitais e de inteligência artificial como apoio ao desenvolvimento de projetos, sempre revisando e testando os resultados.", body_style))

story.append(Paragraph("EXPERIÊNCIA", section_style))
experience = [
    [Paragraph("Jovem Aprendiz — Supermercado", body_style), Paragraph("Aproximadamente 1 ano e 4 meses", meta_style)],
    [Paragraph("• Reposição e organização de mercadorias.<br/>• Apoio nas rotinas de padaria e organização de produtos.<br/>• Atendimento ao cliente e apoio na operação de caixa.<br/>• Organização do ambiente e cumprimento de tarefas operacionais.", small_style), ""],
]
t = Table(experience, colWidths=[112*mm, 55*mm], hAlign="LEFT")
t.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 2)]))
story.append(t)

story.append(Paragraph("FORMAÇÃO", section_style))
story.append(Paragraph("Escola Basilio Bosniac — Carapicuíba, SP<br/>Ensino médio em andamento.", body_style))

story.append(Paragraph("CERTIFICADOS E ESTUDOS", section_style))
story.append(Paragraph("• SENAI — Excel com IA Generativa, em andamento.<br/>• CIEE — Capacitação de Aprendiz em Processos, em andamento.<br/>• MicroMaker — Excel, Word, PowerPoint, Photoshop, CorelDRAW e Marketing.", body_style))

story.append(Paragraph("HABILIDADES", section_style))
story.append(Paragraph("• Organização, pontualidade e responsabilidade.<br/>• Proatividade e facilidade de aprendizagem.<br/>• Atendimento ao cliente e trabalho em equipe.<br/>• Pacote Office: Word e PowerPoint; Excel em desenvolvimento.<br/>• Conhecimentos básicos de design gráfico.<br/>• Interesse e estudos em tecnologia, programação, automação e inteligência artificial.", body_style))

story.append(Spacer(1, 6))
story.append(Paragraph("Documento preparado para divulgação profissional. Esta versão remove o endereço residencial e os contatos de responsáveis presentes no currículo original.", meta_style))

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=16*mm, bottomMargin=14*mm, title="Currículo público — Rickelme Gouveia", author="Rickelme Gouveia")
doc.build(story)
print(OUT)
