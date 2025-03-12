class BungeoppangShop:
    def __init__(self):
        self.stock = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [10, 8, 5]))
        self.prices = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [1000, 1200, 1500]))
        self.sales = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [0, 0, 0])) 

    def check_stock(self):
        for kind, stock in self.stock.items():
            print(f'{kind} 재고: {stock}')

    def process_order(self, bread_type, bread_count):
        try: 
            if bread_type not in self.stock:
                raise KeyError
            
            if not isinstance(bread_count, int):
                raise ValueError


            if self.stock[bread_type] >= bread_count:
                self.stock[bread_type] -= bread_count
                self.sales[bread_type] += bread_count 

            else: 
                print(f'앗! {bread_type}은 재고가 부족합니다 🥺')

        except KeyError: 
            print("올바른 붕어빵 이름을 입력해 주세요! 🙇🏻‍♂️  예시: 초코붕어빵")
        except ValueError:
            print("수량은 숫자로만 입력해 주세요! 🙇🏻‍♂️ 예시: 5")

    def admin_mode(self, bread_type, additional_stock):
        if bread_type in self.stock:
                if isinstance(additional_stock, int) and additional_stock >= 1:
                    self.stock[bread_type] += additional_stock
                    print(f'{bread_type}의 재고가 {additional_stock}만큼 추가되었습니다 🧙🏻 ')
                else:
                    print("추가할 수량은 1 이상의 숫자로만 입력해 주세요! 😎 예시: 5")

        else: 
            print("올바른 붕어빵 종류를 입력해 주세요! 😎 예시: 초코붕어빵")

    def calculate_total_sales(self):
        revenue = 0
        for bread_type in self.sales:
            total_sales = self.sales[bread_type] * self.prices[bread_type]
        print(f"💰 총 매출: {revenue}원 💰")


def main():
    # BungeoppangShop 객체 생성 
    bungeoppang = BungeoppangShop()

    # 사용자에게 모드 선택을 요청 
    mode = input("주문을 하실 경우 '1'을, 관리자일 경우 '2'를 입력하세요: ")

    # 주문 모드 
    if mode == "1":
         while True: 
            bread_type = input("붕어빵 종류를 입력해 주세요(예시: 팥붕어빵, 슈크림붕어빵, 초코붕어빵): \n 종료를 원하실 경우 '종료'를 입력해 주세요. ")
            
            if bread_type == "종료":
                break

            # try, except를 main에다 구현해야 할 듯...
            bread_count = int(input("주문하실 붕어빵의 수량을 숫자로 입력해 주세요(예시: 5): "))
            bungeoppang.process_order(bread_type, bread_count)
           

         # 관리자 모드 
    elif mode == "2":
         while True:
            bread_type = input("추가할 붕어빵 종류를 입력해 주세요(예시: 초코붕어빵): ")

            if bread_type == "종료":
                bungeoppang.calculate_total_sales()
                break
        
            try:
                additional_stock = int(input("추가할 붕어빵의 수량을 입력해 주세요(예시: 5): "))
                bungeoppang.admin_mode(bread_type, additional_stock)
            except ValueError:
                print("수량은 숫자로만 입력해 주세요! 예시: 5")


# main 함수 호출 
if __name__ == "__main__":
    main()           