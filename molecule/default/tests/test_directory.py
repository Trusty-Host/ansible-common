"""Role testing files using testinfra."""

def test_fastdl_directory(host):
    dir_path = "/etc/ansible/facts.d"
    assert host.file(dir_path).is_directory, f"Папка {dir_path} должна существовать"
    assert host.file(dir_path).user == "root", f"Владелец папки {dir_path} должен быть пользователь root"
    assert host.file(dir_path).group == "root", f"Группа папки {dir_path} должна быть root"
