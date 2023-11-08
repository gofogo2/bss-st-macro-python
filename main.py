import pyautogui as pag

while True:
    print('status - 앱 켜짐 체크')
    sizeIcon = pag.locateOnScreen('1.png')
    sizeIcon = pag.locateOnScreen('1-1.png')
    
    if sizeIcon is not None:
        print('status - 앱 켜짐')
        sizeIcon3 = pag.locateOnScreen('4.png')
        print('status - 앱 자동화 상태 체크')
        if sizeIcon3 is not None: # 자동화 상태 확인
            print('status - 앱 자동화 탭 비활성화')
            point = pag.center(sizeIcon3)
            pag.click(point)
            print('status - 앱 즐겨찾기 : action- 앱 자동화 선택')
            pag.sleep(1)
            sizeIcon4 = pag.locateOnScreen('7.png')
            
            if sizeIcon4 is not None:
                point = pag.center(sizeIcon4)
                pag.click(point)
                print('status - 앱 탭 활성화 : action- 앱 탭 비활성화')
            else:
                print('status - 앱 켜짐 2')
        else:
            print('status - 앱 자동화 탭 활성화')
            sizeIcon4 = pag.locateOnScreen('7.png')
            if sizeIcon4 is not None:
                point = pag.center(sizeIcon4)
                pag.click(point)
                print('status - 앱 탭 활성화 : action- 앱 탭 비활성화')
            else:
                print('status - 앱 켜짐 2')
    else: # 앱이 꺼져있다면
        print('status - 앱 꺼짐')
        sizeIcon2 = pag.locateOnScreen('2.png')
        if sizeIcon2 is not None:
            
            point = pag.center(sizeIcon2)
            pag.click(point)
            print('status - 앱 꺼짐 : action- 앱 실행')
        else:
            print('status - 하단에 아이콘을 찾을 수 없음')
    pag.sleep(2)