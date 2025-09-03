tasks = []

def show_menu():
    print("\n--- Yapılacaklar Uygulaması ---")
    print("1. Görev ekle")
    print("2. Görevleri listele")
    print("3. Çıkış")

while True:
    show_menu()
    choice = input("Seçimin: ")

    if choice == "1":
        task = input("Görev gir: ")
        tasks.append(task)
        print(f"✅ '{task}' eklendi.")
    elif choice == "2":
        print("\n--- Görevler ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("👋 Çıkılıyor...")
        break
    elif choice == "4":
        print("👋 çıkış...")
        break
    else:
        print("❌ Geçersiz seçim!")
