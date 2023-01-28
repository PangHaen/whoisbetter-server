# Who Is Better?

---
### FastAPI 실행 방법
```shell
uvicorn main:app --reload 
```

### requirements.txt 생성 방법
```shell
pip3 freeze > requirements.txt
```
위처럼 진행했을 때, requirements.txt 내부에 @ file과 같은 형식으로 버전이 저장되는 경우,
```shell
pip3 list --format=freeze > requirements.txt
```
### requirements.txt 설치 방법
```shell
pip3 install -r requirements.txt
```



