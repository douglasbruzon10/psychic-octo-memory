projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_horas = input("Digite o valor da horas Trabalhada: ")
prazo_estimado = input("Digite o prazo estimado:")

valor_total = int(horas_estimadas) * int(valor_horas)

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_horas)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")
