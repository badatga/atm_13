# balance : 초기 잔액을 설정하는 변수를 초기화
# 금액은 임의 설정
#
# 
# 입금 출금 종료 입출금내역영수증 4가지 기능을 사용할 수 있는 버튼 만들기


balance = 0;

while True:
    num = input('사용하실 기능을 입력하세요 : 1.입금 2.출금 3.영수증보기 4.종료 ')

    if num == '4':
        break
    if num == '1':
        pass
    if num == '2':
        pass
    if num == '3':
        pass

print(f'서비스를 종료합니다. 현 잔액은 {balance}')
