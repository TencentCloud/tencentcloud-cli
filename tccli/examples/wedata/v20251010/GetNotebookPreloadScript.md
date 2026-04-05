**Example 1: 请求成功**



Input: 

```
tccli wedata GetNotebookPreloadScript --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --FileId divetest1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CosURL": "https://bucket-30-251436191.cos.ap-guangzhou.myqcloud.com/sci/17623497097012366/personal/600000561778/6f20e4b5-f2ec-4cb1-a807-79dd88a811a9//notebook_preload_script.py",
            "Script": "from wedata_pre_code.wedata3.client import Wedata3PreCodeClient\n\n# 初始化客户端\nclient = Wedata3PreCodeClient(\n    workspace_id=\"17623497097012366\",\n    mlflow_tracking_uri=\"http://21.78.37.167:5000\",\n    base_url=\"https://ap-guangzhou.wedata.cloud.tencent.com\",\n    region=\"ap-guangzhou\",\n    ap_region_id=int(\"\"),\n    gateway_url=\"\",\n    mlflow_proxy_ip=\"\",\n    mlflow_proxy_port=\"\",\n    feast_proxy_ip=\"\",\n    feast_proxy_port=\"\",\n    kernel_task_name=\"divetest1\",\n    kernel_task_id=\"\",\n    kernel_submit_form_workflow=\"studio\",\n    cloud_sdk_secret_id=\"\",\n    cloud_sdk_secret_key=\"\",\n    cloud_sdk_secret_token=\"\",\n    qcloud_uin=\"600000561778\",\n    qcloud_subuin=\"600000561778\",\n)\n\nclient.init()"
        },
        "RequestId": "61816d8f-e661-4f7e-99ee-6bf48026e735"
    }
}
```

