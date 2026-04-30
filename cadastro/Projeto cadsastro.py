import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- FUNÇÕES ---
def fazer_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    # Verificação simples
    if usuario == "Enzo" and senha == "123456":
        resultado_login.configure(text="Login realizado!", text_color="green")
    else:
        resultado_login.configure(text="Login inválido!", text_color="red")

# --- CONFIGURAÇÃO DA JANELA ---
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("400x450")

# --- INTERFACE (UI) ---
label_titulo = ctk.CTkLabel(app, text="Bem-vindo", font=("Roboto", 24))
label_titulo.pack(pady=20)

# Campo de Usuário
label_user = ctk.CTkLabel(app, text="Usuário:")
label_user.pack(pady=5)
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário", width=200)
campo_usuario.pack(pady=5)

# Campo de Senha
label_pass = ctk.CTkLabel(app, text="Senha:")
label_pass.pack(pady=5)
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", width=200, show="*")
campo_senha.pack(pady=5)

# Botão de Login
botao_login = ctk.CTkButton(app, text="Entrar", command=fazer_login)
botao_login.pack(pady=20)

# Feedback do Login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

# --- INICIALIZAÇÃO ---
app.mainloop()