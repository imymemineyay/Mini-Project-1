##################    현지인 - 사용자별 스킨케어 추천 시스템    ################## 






##############   라이브러리 불러오기   ############## 
## DB 연동
import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       database ='cosmetic_products',
                       port=3306, 
                       user='local_people', 
                       password='local_PP1', 
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor) 
cursor = conn.cursor()


## 회원 정보 저장 및 타임 슬립
import re
customerList = dict()

from time import sleep







##############     전체 완성 코드    ############## 

class Cosmetic:


    def __init__(self, _id='', pwd='', name='', gender='', tel='', old='', skin=''):
        self._id = _id
        self.pwd = pwd
        self.name = name
        self.gender = gender
        self.old = old
        self.tel = tel
        self.skin = skin
        self.login = False
        self.control = True
        self.control2 = True

    def menu_list(self):
        print("\n","➖"*13,"J O I N","➖"*13)
        if self.login == False:
            print("1. 로그인")
        else:
            print("1. 로그아웃")
        print("2. 회원가입")
        print("3. 메인 메뉴")
        print("4. 프로그램 종료")
        print("➖"*30,"\n")
        self.disp_info()

  
    def menu_list2(self):
        print("\n","➖"*9,"S K I N C A R E  S E R V I C E","➖"*9)
        print("1. 스킨케어 추천 서비스")
        print("2. 연령별 화장품 리스트 보기")
        print("3. 피부타입별 화장품 리스트 보기")
        print("4. 모든 화장품 리스트 보기")
        print("5. 이전 결과 리스트 보기")
        if self.login == False:
            print("6. 로그인, 회원가입 메뉴")
        else:
            print("6. 로그아웃")
        print("7. 종료")
        print("➖"*30,"\n")
        self.disp_info()

        
# menu_list(JOIN메뉴)와 연동       
    def menu1(self):
        self.menu_list()
        while True:
            menu1 = input("번호를 선택해 주세요 ▶ ")
            if menu1 == '1':
                self.login_logout()
                self.menu_list()
            elif menu1 == '2':
                if self.login == False:
                    print("회원가입합니다")
                    self.set_id1()
                    self.save_mem()
                    self.login = True
                    self.menu_list()
                else:
                    print("로그인 중입니다.")
            elif menu1 == '3':
                print("메인 메뉴로 이동합니다")
                self.menu_list2()
                break
            elif menu1 == '4':
                print("프로그램을 종료합니다.", end="")
                self.control = False
                break
            else:
                print("잘못 입력하셨습니다.")


# menu_list2(skincare service메뉴)와 연동. 
    def menu2(self):
        self.menu_list2()
        while self.control:
            menu2_num = input("번호를 입력해 주세요 ▶ ")
            if self.login == False:  # 로그인 없이 클릭할 시 출력창
                if menu2_num == '1':
                    print("서비스를 이용하기 위해서는 로그인이 필요합니다.")
                elif menu2_num == '2':
                    print("서비스를 이용하기 위해서는 로그인이 필요합니다.")
                elif menu2_num == '3':
                    print("서비스를 이용하기 위해서는 로그인이 필요합니다.")
                elif menu2_num == '4':
                    print("서비스를 이용하기 위해서는 로그인이 필요합니다.")
                elif menu2_num == '5':
                    print("서비스를 이용하기 위해서는 로그인이 필요합니다.")
                elif menu2_num == '6':
                    self.menu1()
                elif menu2_num == '7':
                    print("프로그램을 종료합니다.")
                    break
                else:
                    print("잘못 입력하셨습니다.")

            elif self.login == True: # 로그인 후 클릭시 연동되는 기능
                if menu2_num == '1':
                    self.choose_sex()
                    self.menu_list2()
                elif menu2_num == '2':
                    self.old_all()
                    self.menu_list2()
                elif menu2_num == '3':
                    self.skin_typeall()
                    self.menu_list2()
                elif menu2_num == '4':
                    self.cosmetic_all()
                    self.menu_list2()
                elif menu2_num == '5':
                    self.myresult()
                    self.menu_list2()
                elif menu2_num == '6':
                    if self.login == False:
                        self.menu1()
                    else:
                        self.logout_menu()
                        self.menu_list2()
                        print("로그아웃 되었습니다.")
                elif menu2_num == '7':
                    print("프로그램을 종료합니다.")
                    break
                else:
                    print("잘못 입력하셨습니다.")

                    
    def set_id1(self): # 아이디 입력 함수
        while True:
            self._id = input("아이디를 입력해 주세요 ▶ ")
            if self.check_id() == True:
                break
        self.setPwd()

    def check_id(self): # 아이디 유효성 검사
        if self._id not in customerList:
            if len(re.findall("[a-z]+", self._id)) == 0 or len(re.findall("[A-Z]", self._id)) != 0 or len(
                    re.findall("[0-9]", self._id)) == 0:
                print("규격에 맞지않습니다.")
                print("영어소문자와 숫자로 작성해주십시오.")
                return False
            elif len(self._id) < 6 or len(self._id) > 12:
                print("아이디의 길이는 6자리이상 12자리 이하로 설정해주십시오.")
                return False
            else:
                print("올바른 형식입니다.")
                return True
        else:
            print("이미 존재하는 아이디입니다.")

    def setPwd(self): # 비밀번호 입력 함수
        while True:
            self.pwd = input("비밀번호를 입력해 주세요 ▶ ")
            if self.pwd_check() == True:
                break
        while True:
            dcheck = input("다시한번 입력해 주세요 ▶ ")
            if self.pwd == dcheck:
                break
            else:
                print("잘못 입력하였습니다.")
        self.set_name()

    def pwd_check(self): # 비밀번호 유효성 검사

        # 문자의 길이 체크
        if len(self.pwd) < 6 or len(self.pwd) > 12:
            print(self.pwd, "의 길이가 적당하지 않습니다.")
            return False

        # 숫자와 영문자로만 구성되어야 한다.
        elif re.findall("[a-zA-Z0-9]+", self.pwd)[0] != self.pwd:
            print(self.pwd, "숫자와 영문자로만 구성되어야 합니다.")
            return False

        # 영문자는 대문자와 소문자가 포함되어야 한다.
        elif len(re.findall("[a-z]", self.pwd)) == 0 or len(re.findall("[A-Z]", self.pwd)) == 0 or len(
                re.findall("[0-9]", self.pwd)) == 0:
            print(self.pwd, "대문자 또는 소문자가 모두 필요합니다.")
            return False

        print(self.pwd, "올바른 형식의 비밀번호 입니다.")
        return True

    def set_name(self): # 이름 입력 및 유효성 검사 함수
        while True:
            n = input("이름 ▶ ")
            if len(re.findall("[a-z]", n)) != 0 or len(re.findall("[A-Z]", n)) != 0 or len(re.findall("[0-9]", n)) != 0 or len(re.findall('[\W]+', n)) != 0 :
                print("규격에 맞지않습니다.")
                print("한글로 작성해주십시오.")
            else:
                print("올바른 형식입니다.")
                self.name = n
                break
        self.set_tel()

    def set_tel(self): # 전화번호 입력 및 유효성 검사 함수
        while True:
            t = input("전화번호 ▶  ")
            print("000-0000-0000 규격으로 입력해주세요.")
            if re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', t):  # 숫자 3개-4개-4개 패턴
                print("회원등록이 완료되었습니다.")
                self.tel = t
                break
            else:
                print("다시 입력해주세요.")
        self.show_info()

    def save_mem(self): # 회원정보를 리스트에 담는 함수
        customerList[self._id] = [self.pwd, self.name, self.tel, self.gender, self.old, self.skin]

    def show_info(self): # 회원가입 완료 후 회원 정보 출력 함수
        print("\n", "귀하의 가입정보는\n 아이디 : {}\n 비밀번호 : {}\n 이름 :{}\n 전화번호 : {}입니다.".format(self._id, self.pwd, self.name,
                                                                                       self.tel))

    def disp_info(self): # 프로그램 실행시 하단에 표시되는 로그인 중인 회원정보(입력하지 않으면 공란이 뜸)
        print("\t\t\t      🔹🔷🔹","접속 정보","🔹🔷🔹")
        print("아이디: {}  비밀번호: {}  이름: {}  전화번호: {}입니다.\n".format(self._id, self.pwd, self.name, self.tel))

    def choose_sex(self):  # 성별고르는 함수명
        print("➖" * 11, '스킨케어 추천 서비스', "➖" * 11, '\n')
        while True:
            a = input("🟠 성별을 입력해주세요 1.여자  2.남자 ▶ ")
            if a == '1':
                self.gender = '여자'

                self.choose_age()
                self.choose_skin()
                customerList.get(self._id)[3] = self.gender
                customerList.get(self._id)[4] = self.old
                customerList.get(self._id)[5] = self.skin
                break

            elif a == '2':
                self.gender = '남자'
                self.choose_age()
                self.choose_skin()
                customerList.get(self._id)[3] = self.gender
                customerList.get(self._id)[4] = self.old
                customerList.get(self._id)[5] = self.skin
                break

            else:
                print("다시 입력해주세요")
        self.survey_summary()

    def choose_age(self):  # 나이대를 고르는 함수
        while True:
            b = input("🟡 나이대를 입력해주세요 1.10대  2.20대  3.30대  4.40대+ ▶  ")
            if b == '1':
                self.old = '10대'
                break
            elif b == '2':
                self.old = '20대'
                break
            elif b == '3':
                self.old = '30대'
                break
            elif b == '4':
                self.old = '40대'
                break
            else:
                print("다시 입력해주세요")

    def choose_skin(self):  # 피부타입을 고르는 함수
        while True:
            c = input("🟢 피부타입을 입력해주세요 1.건성  2.지성  3.민감성 ▶ ")
            if c == '1':
                self.skin = '건성'
                break
            elif c == '2':
                self.skin = '지성'
                break
            elif c == '3':
                self.skin = '민감성'
                break
            else:
                print("다시 입력해주세요")

                # 현재 선택한 항목 출력

    def survey_summary(self): # 선택지 내역 출력 및 결과이동 함수
        print("➖" * 30)
        print("\n", self.name + "은 {0}, {1}, {2}를 선택하셨습니다.".format(self.gender, self.old, self.skin))
        while True:
            survey_result = input('결과를 보러 가시겠습니까? 1. Yes  2. No ▶ ')
            if survey_result == '1':
                self.result()
                break
            elif survey_result == '2':
                break
            else:
                print('다시 입력하세요')

    def result(self): # 결과 값 제출 함수 (오라클 연동)
        print("\n", "➖" * 12, "💌 결과 💌", "➖" * 13)
        print()
        if self.gender == '여자' and self.old == '10대' and self.skin == '건성':
            sql1 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%10대%' and type like '%건성%'"
            cursor.execute(sql1)
            for row in cursor:
                print(row)
        elif self.gender == '여자' and self.old == '10대' and self.skin == '지성':
            sql2 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%10대%' and type like '%지성%'"
            cursor.execute(sql2)
            for row in cursor:
                print(row)
        elif self.gender == '여자' and self.old == '10대' and self.skin == '민감성':
            sql3 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%10대%' and type like '%민감성%'"
            cursor.execute(sql3)
            for row in cursor:
                print(row)
        elif self.gender == '여자' and self.old == '20대' and self.skin == '건성':
            sql4 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%20대%' and type like '%건성%'"
            cursor.execute(sql4)
            for row in cursor:
                print(row)
        elif self.gender == '여자' and self.old == '20대' and self.skin == '지성':
            sql5 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%20대%' and type like '%지성%'"
            cursor.execute(sql5)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '20대' and self.skin == '민감성':
            sql6 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%20대%' and type like '%민감성%'"
            cursor.execute(sql6)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '30대' and self.skin == '건성':
            sql7 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%30대%' and type like '%건성%'"
            cursor.execute(sql7)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '30대' and self.skin == '지성':
            sql8 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%30대%' and type like '%지성%'"
            cursor.execute(sql8)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '30대' and self.skin == '민감성':
            sql9 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%30대%' and type like '%민감성%'"
            cursor.execute(sql9)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '40대' and self.skin == '건성':
            sql10 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%40대%' and type like '%건성%'"
            cursor.execute(sql10)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '40대' and self.skin == '지성':
            sql11 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%40대%' and type like '%지성%'"
            cursor.execute(sql11)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)
        elif self.gender == '여자' and self.old == '40대' and self.skin == '민감성':
            sql12 = "select name, price, company from cosmetic_product where gender like '%여자%' and age like '%40대%' and type like '%민감성%'"
            cursor.execute(sql12)
            for row in cursor:  # 커서가 가리키는 1개의 레코드를 row에 저장
                print(row)

        elif self.gender == '남자' and self.old == '10대' and self.skin == '건성':
            sql13 = "select name, price, company from cosmetic_product where gender like '%self.gender%' and age like '%self.old%' and type like '%self.skin%'"
            cursor.execute(sql13)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '10대' and self.skin == '지성':
            sql14 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%10대%' and type like '%지성%'"
            cursor.execute(sql14)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '10대' and self.skin == '민감성':
            sql15 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%10대%' and type like '%민감성%'"
            cursor.execute(sql15)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '20대' and self.skin == '건성':
            sql16 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%20대%' and type like '%건성%'"
            cursor.execute(sql16)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '20대' and self.skin == '지성':
            sql17 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%20대%' and type like '%지성%'"
            cursor.execute(sql17)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '20대' and self.skin == '민감성':
            sql18 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%20대%' and type like '%민감성%'"
            cursor.execute(sql18)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '30대' and self.skin == '건성':
            sql19 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%30대%' and type like '%건성%'"
            cursor.execute(sql19)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '30대' and self.skin == '지성':
            sql20 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%30대%' and type like '%지성%'"
            cursor.execute(sql20)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '30대' and self.skin == '민감성':
            sql21 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%30대%' and type like '%민감성%'"
            cursor.execute(sql21)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '40대' and self.skin == '건성':
            sql22 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%40대%' and type like '%건성%'"
            cursor.execute(sql22)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '40대' and self.skin == '지성':
            sql23 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%40대%' and type like '%지성%'"
            cursor.execute(sql23)
            for row in cursor:
                print(row)
        elif self.gender == '남자' and self.old == '40대' and self.skin == '민감성':
            sql24 = "select name, price, company from cosmetic_product where gender like '%남자%' and age like '%40대%' and type like '%민감성%'"
            cursor.execute(sql24)
            for row in cursor:
                print(row)
        else:
            print("죄송합니다. 상품의 자료를 구축중입니다. 다음에 시도해주세요:(")

    def myresult(self):  # 이전에 조회한 결과 보기 함수
        if self.skin == '':
            print("이전 검사 결과가 없습니다. 메뉴로 돌아갑니다.")
        else:
            print(self.name + '님은 {}, {}, {}를 선택하셨습니다.'.format(self.gender, self.old, self.skin))
            while True:
                a = input('이전 내 결과를 기반으로 추천 서비스를 받으시겠습니까? [1] Y [2] N')
                if a == '1':
                    self.result()
                    break
                elif a == '2':
                    break
                else:
                    print('다시 입력해 주세요')

    def skin_typeall(self):  # 타입별 아이템 보기 함수
        while True:
            e = input("🟢 피부타입을 입력해주세요 1.건성  2.지성  3.민감성 ▶ ")
            if e == '1':

                sql25 = "select name, price, company from cosmetic_product where type like '%건성%'"
                cursor.execute(sql25)
                for row in cursor:
                    print(row)
                break
            elif e == '2':

                sql26 = "select name, price, company from cosmetic_product where type like '%지성%'"
                cursor.execute(sql26)
                for row in cursor:
                    print(row)
                break
            elif e == '3':

                sql27 = "select name, price, company from cosmetic_product where type like '%민감성%'"
                cursor.execute(sql27)
                for row in cursor:
                    print(row)
                break
            else:
                print("다시 선택해주세요.")

    def old_all(self): # 나이별 아이템 보기 함수
        print("➖" * 10, '나이별 화장품 전체보기', "➖" * 11, '\n')
        while True:
            a = input('🟡 나이대를 입력해주세요 1.10대  2.20대  3.30대  4.40대+ ▶  ')
            if a == '1':
                sql30 = "select name, price, company from cosmetic_product where age like '%10대%'"
                cursor.execute(sql30)
                for row in cursor:
                    print(row)
                break
            elif a == '2':
                sql31 = "select name, price, company from cosmetic_product where age like '%20대%'"
                cursor.execute(sql31)
                for row in cursor:
                    print(row)
                break
            elif a == '3':
                sql32 = "select name, price, company from cosmetic_product where age like '%30대%'"
                cursor.execute(sql32)
                for row in cursor:
                    print(row)
                break
            elif a == '4':
                sql33 = "select name, price, company from cosmetic_product where age like '%40대%'"
                cursor.execute(sql33)
                for row in cursor:
                    print(row)
                break

            else:
                print('다시 입력해주세요')

    def cosmetic_all(self): # 전체 화장품 리스트 출력 함수
        print("➖" * 10, '🖤 모든 화장품 전체보기 🖤', "➖" * 10, '\n')
        sql34 = "select name, price, company from cosmetic_product"
        cursor.execute(sql34)
        for row in cursor:
            print(row)

    def login_logout(self): # 로그인, 로그아웃 함수
        if self.login == False:
            print("로그인 합니다.")
            self.login_menu()
        else:
            print("로그아웃 합니다.")
            self.logout_menu()
            self.menu_list()

    def login_menu(self): # 로그인 함수
        self.control2 = True
        while self.control2:
            uid = input('아이디를 입력해 주세요 ▶ ')
            if uid in customerList.keys():
                i =1
                for i in range(1, 4):
                    pwd = input('비밀번호 ▶ ')
                    if customerList.get(uid)[0] == pwd:
                        self._id = uid
                        self.pwd = customerList.get(uid)[0]
                        self.name = customerList.get(uid)[1]
                        self.tel = customerList.get(uid)[2]
                        self.gender = customerList.get(uid)[3]
                        self.old = customerList.get(uid)[4]
                        self.skin = customerList.get(uid)[5]
                        self.login = True
                        print("로그인 되셨습니다.")
                        break
                    elif pwd == "종료":
                        print("메뉴로 돌아갑니다.")
                        self.control2 = False
                        break
                    else:
                        print("비밀번호를 %d회 잘못 입력 하였습니다." % i)
                if i == 3:
                    print("")
                    print("부정한 접속 시도가 감지되었습니다.")
                    print("5초간 시스템 사용이 불가능 합니다.")
                    sleep(5)
                    print("이제 시스템 사용이 가능합니다.")
                    break
                break    
            elif uid == '종료':
                print("메뉴로 돌아갑니다.")
                break
            else:
                print("ID가 존재하지 않습니다.")
                print("메뉴로 돌아가시려면 '종료'를 입력해 주세요")

    def logout_menu(self): # 로그아웃 함수
        self._id = ""
        self.pwd = ''
        self.name = ''
        self.tel = ''
        self.gender = ''
        self.old = ''
        self.skin = ''
        self.login = False
        
        
        
        
        
        
        
##############    코드 실행   ##############        
        
        
a = Cosmetic()
a.menu2()


