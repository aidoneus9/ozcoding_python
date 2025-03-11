# 재고
storage = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [10, 8, 5]))
# 가격
price = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [1000, 1200, 1500]))
# 판매 
sold = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [0, 0, 0]))

# 주문 받기
while True: 
    order_kind = input("붕어빵 종류를 입력하세요(종료하려면 '종료' 입력): ") # 문자열 
    
    if order_kind == "종료":

        # 매출 관리
        revenue = 0

        for key in sold:
            revenue += sold[key] * price[key]

        print(f'총 매출: {revenue}')
        
        break

# 손님의 주문 내역 
    order_number = int(input("붕어빵 개수를 입력하세요: ")) # 문자열 -> 정수형으로 변환 
    
    order = {order_kind: order_number} # dictionary 
    print("주문 내역:", order)

    
# 주문 처리
    if order_kind in storage:
        if order_number > storage[order_kind]:
            print(f'주문하신 {order_kind}은 재고가 부족합니다 🥲')
            print(f'현재 재고: {storage}, 판매한 붕어빵 맛과 개수: 없음')
        else:
            storage[order_kind] -= order_number
            sold[order_kind] += order_number
            print(f'현재 재고: {storage}, 판매한 붕어빵 맛과 개수: {sold}')
            
# # 매출 
# revenue = 0

# for key in sold:
#     revenue += sold[key] * price[key]

# print(f'총 매출: {revenue}')

################################################################################
# 관리자 모드 
# storage = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [10, 8, 5]))

# while True:
#     add_kind = input("추가할 붕어빵의 종류를 입력하세요(종료하려면 '종료' 입력): ")
    
#     if add_kind == "종료":
#         break
    
#     add_number = int(input(f'추가할 {add_kind}의 개수를 입력하세요: '))

#     # 추가된 재고 업데이트하기 
#     storage[add_kind] += add_number  
#     print(f'현재 재고: {storage}')

##################################################################################
# # 매출 관리 
# # 각 붕어빵의 가격 
# price = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [1000, 1200, 1500]))

# # 붕어빵의 매출 
# revenue = 0

# for key in sold:
#     revenue += sold[key] * price[key]

# print(revenue)