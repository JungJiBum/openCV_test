# https://bskyvision.com/entry/python-cv2imread-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%BC-%EA%B2%BD%EB%A1%9C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EB%AA%BB%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95
import cv2      # print(cv2.__version__)    4.6.0
import numpy as np
'''
시나리오
1. 웹툰 검색
2. 대칭 입력
3. 색 입력
'''
'''
처음 시도했던 방법은 target에서 웹툰 제목을 입력하였으나, 문자열 인식에러로 인해 에러발생
path = "이미지 폴더 경로"
target = input("찾고자하는 이미지를 적어주세요. : ")
img = cv2.imread(path + '/' + target + '.jpg')

따라서 새로운 방법을 찾아서 적용함
img_array = np.fromfile(full_path,np.uint8)
    np.fromfile()함수를 이용하여 바이너리 데이터를 넘파이 행렬로 읽어옴
img_color = cv2.imdecode(img_array,cv2.IMREAD_COLOR)
    cv2.imdecode()함수로 복호화하여 openCV에서 사용할수 있는 형태로 변경
'''

path = "이미지폴더경로"
c = ''
f = ''
r = ''

def search_webtoon():
    name = input("찾고자 하는 웹툰을 입력하세요 : ")
    full_path = path + '/' + name + '.jpg'
    #넘파이 행렬로 생성
    img_array = np.fromfile(full_path, np.uint8)
    #함수호출
    choose_style(img_array)


def choose_style(img_arr):
    style = input("원하는 출력을 확인해주세요.(컬러,흑백,기타) : ")
    choice(img_arr, style)

    menu = input("어떤 작업을 하실 생각이십니까?(좌우,상하, 상하좌우) : ")
    flip(menu, c)

    angle = input("몇도 회전 시킬겁니까?(90, 180, 270) : ")
    rotate(angle,f)

def rotate(angle,f):
    global r
    r = cv2.rotate(f,cv2.ROTATE_90_CLOCKWISE) if angle=='90'else cv2.rotate(f,cv2.ROTATE_180)if angle=='180'else cv2.rotate(f,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('test',r)
    end()

def choice(url, style):
    global c
    # if style == "컬러":
    #     img_color = cv2.imdecode(url, cv2.IMREAD_COLOR)
    #     r = img_color
    # elif style == "흑백":
    #     img_gray = cv2.imdecode(url, cv2.IMREAD_GRAYSCALE)
    #     r = img_gray
    # else:
    #     img_unchanged = cv2.imdecode(url, cv2.IMREAD_UNCHANGED)
    #     r = img_unchanged
    # return r
    c = cv2.imdecode(url,cv2.IMREAD_COLOR) if style=='컬러' else cv2.imdecode(url,cv2.IMREAD_GRAYSCALE) if style=='흑백'else cv2.imdecode(url,cv2.IMREAD_UNCHANGED)

def flip(menu, img_array):
    global f
    # cv2.imshow('flip',f)
    # end()
    # if menu == "좌우":
    #     flip_horizontal = cv2.flip(img_array, 1)
    #     cv2.imshow('horizontal', flip_horizontal)
    #     end()
    # elif menu == "상하":
    #     flip_vertical = cv2.flip(img_array, 0)
    #     cv2.imshow('vertical', flip_vertical)
    #     end()
    # else:
    #     flip_both = cv2.flip(img_array, -1)
    #     cv2.imshow('both', flip_both)
    #     end()
    f = cv2.flip(img_array,1) if menu=='좌우' else cv2.flip(img_array,0) if menu=='상하' else cv2.flip(img_array,-1)

def end():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


name = search_webtoon()
