**Example 1: 动态资产**



Input: 

```
tccli csip DescribeDynamicAssets --cli-unfold-argument  \
    --Provider tencent \
    --AssetType cvm_instance \
    --MemberId mem-0acb10f2f9a4daee \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By Desc
```

Output: 
```
{
    "Response": {
        "Assets": [
            "aW5zdGFuY2VfaWQvYXNzZXRfbmFtZTo6a*5*LWZocHE*ZWZkL2ds5rWL6K+V*LWE*LqnLS0t5LiK5rW3|aW5zdGFuY2VfdGFnczo6Z2zmtYvor5U6dGVz*DMv5q2j5**PQTrmraPlvI9C|Y3Vz*G9tX3RhZ3M6Og=**Y3*lYXRlZF9h*Do6MT*2OTI0NDEyMzAw*A==|X2NyZWF0ZV*0aW1l*joxNzY5Mjg1MDE2M*k2|Y*BwaWQ*OjEzMDA0*DgwNTg=|**NzZX*f*m**Oj*m*WV*YTdlNGUwZTc*ZD*2ODM4Z**zY2Q0ZWI1MDFmYQ==|aXAvZG9tYWluOjoxMDEuMzUuMTQ0LjE3OC8xOTIuMTY4LjI0LjIxLy8=|cHVibGljX2V4cG9zZTo6MQ==|cmlzazo6MC8wLzAvMC8w|dnBjOjp2cGMtYTFxcGo3YWsvZmVuZ3FxaWFu|cmVn*W9uOjr**Y**uJz*nLDljLoo5LiK5rW*KQ==*cHJvamVj*Do66b*Y6K6k6aG555u*|cHJvdGVjdF9*dG*0dXM6*jEwMQ==*bmV3X3*0YXR*czo66L+Q6KGM5Lit|bmV3X3N0YXR***90eXBlOjpzdWNjZX*z|b3Nfbm*tZTo6VGVuY*VudE*TIFNlcnZlc**0IGZvciB4ODZfN***|aW**Z2*faWQ6Oml**y02bjIxbXNrMQ==|aW1hZ2VfdHlwZTo65YWs5YWx6ZWc5YOP"
        ],
        "Header": [
            {
                "Copy": 1,
                "Filters": [
                    {
                        "Attr": "instance_id",
                        "Label": "资产ID",
                        "LabelEn": "Asset ID",
                        "Style": "text",
                        "Value": "instance_id"
                    }
                ],
                "ItemType": "instance_id/asset_name",
                "Label": "资产ID/资产名称",
                "LinkURL": "",
                "Sort": 0,
                "ValueStyle": "instance_id/asset_name",
                "Values": [
                    "instance_id"
                ]
            }
        ],
        "RegionList": [
            {
                "Text": "华北地区(北京)",
                "Value": "ap-beijing"
            }
        ],
        "TotalCount": 59,
        "RequestId": "ba3aefb5-9ca1-43e2-938e-2e3e5e9b89ef"
    }
}
```

