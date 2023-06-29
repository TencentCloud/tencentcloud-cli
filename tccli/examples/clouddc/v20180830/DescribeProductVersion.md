**Example 1: 产研接口-获取产品信息接口**

交付中心支持的自研产品有一套产品接入流程，通过此流程接入的产品名称和产品版本交付中心才可以支持交付。为了减少产研侧和交付侧的沟通成本，拟以交付侧的产品名称和版本为依据，因此需要天途提供产品名称和版本列表，供产研其他平台引用。
文档链接：https://iwiki.woa.com/pages/viewpage.action?pageId=395934565

Input: 

```
tccli clouddc DescribeProductVersion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "12345",
        "JsonData": "[{\"productId\":10008,\"short\":\"TStack\",\"version\":[\"Kilo\",\"Pike\",\"6.7\",\"6.3\",\"6.5\",\"6.9\",\"6.9\",\"6.9\",\"6.9\",\"6.9\",\"6.9\",\"6.9\"],\"sonProduct\":[]}]"
    }
}
```

