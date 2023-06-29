**Example 1: 产研接口-获取产品项目信息**

解决的TO拆解问题（TO问题关联）或者  自身的规划
界面/逻辑/数据字段/审批流
文档链接：https://iwiki.woa.com/pages/viewpage.action?pageId=395934565

Input: 

```
tccli clouddc DescribeProductProjectInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "12345",
        "JsonData": "[{\"ltc_id\":\"\\u65e0\",\"project_name\":\"\\u5357\\u901a\\u5e02\\u516c\\u5b89\\u5c40POC\",\"order_id\":\"TS373732019-04-01\",\"service_stage\":\"\\u96c6\\u6210\\u4ea4\\u4ed8\",\"service_type\":\"POC\\u6d4b\\u8bd5\",\"product_name\":\"Tstack\",\"customer_name\":\"\",\"game_point\":\"\",\"deliver_version\":\"\",\"progress\":\"100%\"},{\"ltc_id\":\"20191101123189\",\"project_name\":\"\\u5357\\u7f51\\u4e91\\u8f6f\\u4ef6\\u53ca\\u7ec4\\u4ef6\\u4f18\\u5316\\u5b8c\\u5584(\\u7b2c\\u4e00\\u6279)\\u6846\\u67b6\\u91c7\\u8d2d\\u9879\\u76ee\\uff08\\u53051-\\u5357\\u7f51\\u4e91\\u5e73\\u53f0\\u57fa\\u5ea7\\uff09\",\"order_id\":\"TS2020072485868\",\"service_stage\":\"\\u552e\\u540e\\u670d\\u52a1\",\"service_type\":\"\\u8fd0\\u7ef4\\u670d\\u52a1\",\"product_name\":\"TStack\",\"customer_name\":\"\\u4e1c\\u534e\\u8f6f\\u4ef6\\u80a1\\u4efd\\u516c\\u53f8\",\"game_point\":\"\",\"deliver_version\":\"\",\"progress\":\"46.15%\"},{\"ltc_id\":\"20190304113658\",\"project_name\":\"\\u6570\\u5b57\\u5e7f\\u4e1c-\\u817e\\u8baf\\u4e91\\u653f\\u52a1\\u4e91\\u670d\\u52a1\\u6846\\u67b6\\u91c7\\u8d2d\\uff082019\\u5e74\\u7b2c\\u4e00\\u6279\\uff09\",\"order_id\":\"TS2020082892129\",\"service_stage\":\"\\u96c6\\u6210\\u4ea4\\u4ed8\",\"service_type\":\"\\u4ea4\\u4ed8\\u5b9e\\u65bd\",\"product_name\":\"TStack\",\"customer_name\":\"\\u6570\\u5b57\\u5e7f\\u4e1c\\u7f51\\u7edc\\u5efa\\u8bbe\\u6709\\u9650\\u516c\\u53f8\",\"game_point\":\"\",\"deliver_version\":\"6.9\",\"progress\":\"69.23%\"},{\"ltc_id\":\"20200219129392\",\"project_name\":\"\\u4e00\\u4f53\\u5316\\u5e73\\u53f0\\u5efa\\u8bbe\",\"order_id\":\"TE2020090393460\",\"service_stage\":\"\\u96c6\\u6210\\u4ea4\\u4ed8\",\"service_type\":\"\\u4ea4\\u4ed8\\u5b9e\\u65bd\",\"product_name\":\"TStack\",\"customer_name\":\"\\u6c5f\\u82cf\\u7701\\u4eba\\u529b\\u8d44\\u6e90\\u548c\\u793e\\u4f1a\\u4fdd\\u969c\\u5385\",\"game_point\":\"\",\"deliver_version\":\"\\u72ec\\u7acb-141\\u7248\\u672c\",\"progress\":\"53.85%\"}]"
    }
}
```

