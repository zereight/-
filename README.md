네이버 블로그의 텍스트를 크롤링할 수 있는 코드입니다.

네이버 블로그에 스크랩 방지가 되어있어도 상관없습니다.

- 준비물 (무조건 firefox로 해야합니다.)
Firefox, colab, python3

- 실행방법
Crawler.py를 에디터로 열어 keyword, num을 수정해줍니다.

터메널에 python3 1. Crawler.py 를 입력하여 실행시킵니다.

=> 파이어폭스창이 안뜨면 셀레니움 파이어폭스 셋팅을 다시해주세요.

중요) 파이어폭스창이 뜨면 새탭을 열어 about:config를 입력하여 파이어폭스 설정창으로 들어갑니다.
검색창에 java를 입력하고 javascript:enabled를 false로 바꿔준뒤 탭을 닫습니다.

그러면 브라우저창이 뜨고 20초 뒤에 정하신 페이지까지의 블로그들의 주소를 크롤링하고,
블로그 주소에 하나하나 들어가면서 텍스트를 크롤링합니다. (크롤링 하는 도중 복사,붙여넣기작업은 지양해주세요. 크롤링시 문제가 생길수있습니다.)

완료후 data.pickle 데이터가 생깁니다.

주어진 2. 워드클라우드 만들기.ipynb 를 colab에 올려주세요.

또는 https://colab.research.google.com/drive/1g047qzYmY_1-Cfq5ie1qRDu-F6ThmU9l
에 접속하여 사본을 만드세요.

from google.colab import files
uploaded = files.upload()
라는 셀을 실행하여 data.pickle 파일을 업로드해주세요.

한번더 같은 셀을 실행하여 NanumSquareL.ttf 파일을 업로드하세요. 
구글에 검색하거나 폴더에 들어있는것을 쓰셔도 됩니다.

다 했으면 나머지셀들을 실행하면 됩니다. 금지단어는 스스로 추가하세요.