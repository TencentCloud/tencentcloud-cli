**Example 1: 成功**



Input: 

```
tccli iss BatchGetVideoSnapshotImageUrl --cli-unfold-argument  \
    --ImageIds 9e79************************78dff586 \
    --ImageUrlExpires 600
```

Output: 
```
{
    "Response": {
        "Data": {
            "ImageUrlExpires": 600,
            "Images": [
                {
                    "ErrorMessage": "",
                    "ImageId": "9e798***********************78dff586",
                    "ImageUrl": "https://*******************/ipts/image?source=O********BXXILZ********************DI***FU2GEZ*********************WGY3***************************3D**************************3DHE**************************MNBS**********************res=M*********E****************pOzl*************************ZWQwLWRm*****************pires=NjAw*********************xMg&sk=*****W********************FmY*******************&sign=ZT*************************4NzU0**********U"
                }
            ]
        },
        "RequestId": "a05843d1-731c-4369-a87c-71c445819830"
    }
}
```

