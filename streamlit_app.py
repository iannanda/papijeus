# todo.py
# Program To-Do List Sederhana

todo_list = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def show_tasks():
    if not todo_list:
        print("Belum ada tugas.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Masukkan nama tugas: ")
    todo_list.append(task)
    print("Tugas berhasil ditambahkan!")

def delete_task():
    show_tasks()
    try:
        index = int(input("Masukkan nomor tugas yang akan dihapus: "))
        if 0 < index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"Tugas '{removed}' berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar!")

def main():
    while True:
        show_menu()
        choice = input("Pilih menu (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
