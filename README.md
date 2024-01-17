

# chatGpt 根据 用户名、密码 获取access_token 主要是用来自动获取access_token


## 用法
### 启动服务

```
docker-compose up -d
```

### 获取token
```
curl -X POST http://127.0.0.1:3010/get_chatgpt_access_token -d "username=username@mail.com&password=password"
```

返回的值为
```
{"access_token":"accessToken"}
```

## 注意

由于官网的 API 接口有时会调整，可能随时会失效

由于使用的方式为启动一个浏览器模拟登录， 需要跳过多个登录界面和人机验证， 可能会获取失败

由于内置使用的是浏览器模拟登录， docker比较大

