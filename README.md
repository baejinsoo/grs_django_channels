## (GRS 프로젝트 - LCD화면 웹)

## AWS ec2 django-channels 배포

### EC2 setting

1. ec2 인스턴스 시작 (ubuntu 18.04)

2. t2.micro 프리티어 선택

3. 새 보안 그룹 ssh 내ip, 규칙 추가 (사용자 지정TCP, 포트번호 8000,내ip)

4. 시작 및 키페어 저장

5. 고정 ip 할당

6. putty 이용해서 접속 => ubuntu 입력

7. `sudo vi /etc/default/locale`

   ```
   LC_CTYPE="en_US.UTF-8"
   LC_ALL="en_US.UTF-8"
   LANG="en_US.UTF-8"
   ```

8. 1. `sudo apt-get update`
   2. `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev`

9. pyenv 설치

   1. `curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash`

   2. `vi ~/.bashrc`

   3. 파일 맨 아래에 내용 추가

      ```
      export PATH="~/.pyenv/bin:$PATH"
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"
      ```

10. git 설치

    `sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev`

11. srv 폴더 유저 변경

    `sudo chown -R ubuntu:ubuntu /srv/`

12. 프로젝트 `clone` 및 `pyenv` 설정

    1. `git clone 레포지토리.git`
    2. `cd 파일명`
    3. `pyenv install 3.7.0` 장고실행시 파이썬 버전 설치
    4. `pyenv virtualenv 3.7.0 가상환경명` 
    5. `pyenv  local 가상환경명`
    6. `pip install -r requriements.txt`

13. redis-server 설치 및 실행

    `sudo apt-get install redis-server`

    `docker run -p 6379:6379 -d redis:5`

    `python manage.py runserver 0:8000`

    