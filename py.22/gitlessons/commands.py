GIT - распределенная система контроля версии.
Это система для отслеживания и ведения истории изменений ваших файлов или проекта.

Репозиторий - хранилище ваших файлов, которыe вы отслеживаете при помощи гита, и их изменений.

Команды Git:

1. git init - она создает новый гит репозиторий локально на вашем пк, создаст она в той директории где вы запускаете команду.
2. git add - когда мы создаем и изменяем файлы, то при помощи этой команды мы загружаем все изменения в промежуточное место хранение

git add <file_name>
git add . ->  все в текущей директории

3. git commit - как только мы достигаем определенного момента в разработке, то мы тогда сохраняем и комментируем все наши изменения в репозиторий.
(фиксация изменений в репо.)

git commit -m '<comment>'

sudo apt install git - для установки GIT

Для настройки изменений 
git config --global user.name "Iskenderov2001"
git config --global user.email "87mersedes50@gmail.com"
git config --list

ssh-keygen -t rsa

ls -a -> для проверики "rsa"

iskenderov@iskenderov-Nitro-AN515-56:~$ cd .ssh
iskenderov@iskenderov-Nitro-AN515-56:~/.ssh$ ls
id_rsa  id_rsa.pub
iskenderov@iskenderov-Nitro-AN515-56:~/.ssh$ cat id_rsa.pub


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC8s8bhFcnNYM2gOMrT+ga1Ok7NbZ/KM5Xlq3f00slB2nmR4yZ+1xu8w2jLSfpT198HjLgaue6DLe7hlGaFSJ6A3jQ0znB4nYSn6FnX1It584BA0Xa4WTqY1jmq0XCwa5V7V41BPqnrwIrlMFLpBPSM0vjQm2f2Yxw6ioZyccGyS+BtIw97l3/G/Wu8qxZvX5KkCtyEyGHDWECGRQDKefGrDC/Yh9Wmi01CkzzZlOhJksds6WZ53+7o9fUDS46eGB+sFcY7g3CV1nFyPaWBlplJYpNDYVGxK4PfXMNgcivSN2iEaH6IBsR/EW09AX1msOXAx57DGwRvmFVQCTioVIeIUjEq06OFrdXK3ZgRbnweKF8MEj7KIf7/JT7aZSJ+4TygfvXck+418l7+ukXjdsnCPIrotE/u2FD27DPZ87Vbd/E/VfYtqGqZ3ZwVImvJNlEMLSXyLAU/15i2jzZ25gSPVqQFpcFgaEAMNpQ1MKWfxG9upNFX+f4x1sghdIGRJ8E= iskenderov@iskenderov-Nitro-AN515-56
.
git status - проверка статуса изменений.

4. git remote add - это команда для того чтобы связать ваш локальный репозиторий с удаленым репозиторием (репо в гитхабе)
git remote add <название подключения> <ссылка на репозиторий>

git remote add origin <url>

5. git push - после коммита изменений при помощи этой команды мы отправляем наши изменения в файлах на удаленный репозиторий.

git push <origin> <название ветки (main)> 

git push origin main

git branch
.

----------------------------------------------------------------------------------------------
1. git init
2. git branch -M main (переименовываепм главную ветку с master на main)
3. git add .
4. git commit -m 'comment' (всё добавлено в локальный репо)
5. git remote add origin <url>
6. git push origin main
//////////////////////////////////////////
git add .
git commit -m 'comment'
git push origin main


