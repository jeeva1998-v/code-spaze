import tkinter as tk; from tkinter import simpledialog; from reportlab.pdfgen import canvas

def generate_certificate(): 
    root = tk.Tk(); root.withdraw(); 
    name = simpledialog.askstring("Input", "Enter intern's name:"); 
    course = simpledialog.askstring("Input", "Enter course name:"); 
    c = canvas.Canvas(f"{name}_certificate.pdf"); 
    c.drawString(200, 750, "Certificate of Completion"); 
    c.drawString(180, 700, f"This certifies that {name}"); 
    c.drawString(180, 650, f"has successfully completed the {course} course."); 
    c.save(); 
    print(f"Certificate generated for {name}")

generate_certificate()
