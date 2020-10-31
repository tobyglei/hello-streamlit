# Streamlit 在 21云盒子 的示例

这是 [21云盒子](http://www.21yunbox.com/) 上创建的 [Streamlit](https://www.streamlit.io/) 示例。

## 部署

通过以下几步就可以把 Streamlit 跑起来

1. Fork [Streamlit](https://github.com/tobyglei/hello-streamlit)
2. 在21云盒子上创建一个 **云服务**， 并允许21云盒子访问你的代码库
3. 选上 **`Python 3`** 环境
4. 启动指命:  **`streamlit run first_app.py --server.enableCORS=false --server.port=10000 --browser.serverAddress='0.0.0.0' --server.headless=true `**
5. 点"创建"

<img src="screenshot.png">

部署成功后的截图

<img src="https://21box-assets.oss-cn-beijing.aliyuncs.com/deployed_result.png" width="300px">

当构建完成，你的应用将会在21云盒子的子域名能访问。

其他可以部署在21云盒子的示例，请看 [技术文档](https://www.21yunbox.com/docs/v2/)。