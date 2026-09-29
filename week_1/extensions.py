extension = input("File name: ").strip().lower()
match extension:
    case extension if extension.endswith(".gif"):
        print("image/gif")
    case extension if extension.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    case extension if extension.endswith(".png"):
        print("image/png")
    case extension if extension.endswith(".pdf"):
        print("application/pdf")
    case extension if extension.endswith(".txt"):
        print("text/plain")
    case extension if extension.endswith(".zip"):
        print("application/zip")            
    case _:
        print("application/octet-stream")