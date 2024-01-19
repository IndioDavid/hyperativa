def check_file(filename, allowed_extensions:set):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions