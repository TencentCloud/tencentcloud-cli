**Example 1: 场景照篡改检测告警**

门头照

Input: 

```
tccli ocr VerifyScenePhoto --cli-unfold-argument  \
    --Scene 0101 \
    --ImageUrl https://demo-1400073141.cos.ap-guangzhou.myqcloud.com/%E5%85%83%E5%AE%9D.png?q-sign-algorithm=sha1&q-ak=AKID6WpjBeiQeF0RA-TleJJ5oe9uVZAtM4w6oX1k6TKXVVuLpSkq7pNd3draS3XjwHw7&q-sign-time=1776838277;1776841877&q-key-time=1776838277;1776841877&q-header-list=host&q-url-param-list=&q-signature=4cef25001d28d2172825e41f75c2af5bf551014e&x-cos-security-token=xheG1dXFML3tXG5BbL3WBkxVgTMPn53a210e4baed39631a9b75078d24ada5312POGPBv-E8gHNUZW60alPmj_rZ6YYQDrEldc7Vd-Prv9oW4mMNFQT1EXd92m7fxTHnqgjLnAgBMOIfJXdAMF1huLxH8LXhOiJXD9ydvh_tgzegboc_lUSLWebcUBHP4Wbq7pIN_be3zrdHxGvqr1nG1y_ACrwo6iujcbock0-U4fqsvf1R_Z00Xch68U_u51UAr9Kc9fYYD9uVW1JpQCdMKn2A3eFsVEocM8Pvx_BvVGYlr1slpJcYePdieaREOaGdejq_g9aozxuR5P0jNrowA
```

Output: 
```
{
    "Response": {
        "RemakeScreen": {
            "IsWarn": false,
            "RiskConfidence": 0
        },
        "Screenshot": {
            "IsWarn": false,
            "RiskConfidence": 0
        },
        "Synthesis": {
            "IsWarn": false,
            "RiskConfidence": 0
        },
        "Tamper": {
            "IsWarn": true,
            "Polygon": [
                {
                    "LeftBottom": {
                        "X": 262,
                        "Y": 40
                    },
                    "LeftTop": {
                        "X": 262,
                        "Y": 26
                    },
                    "RightBottom": {
                        "X": 317,
                        "Y": 40
                    },
                    "RightTop": {
                        "X": 317,
                        "Y": 26
                    }
                }
            ],
            "RiskConfidence": 0.9999996
        },
        "TextWatermark": {
            "IsWarn": false,
            "RiskConfidence": 0
        },
        "RequestId": "f3a32605-178d-4765-aa48-05b9e0aef048"
    }
}
```

