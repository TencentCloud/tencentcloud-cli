**Example 1: 短音频内容理解同步**

短音频内容理解同步

Input: 

```
tccli gme CreateAudioModerationSync --cli-unfold-argument  \
    --Sdkappid 1410000000 \
    --FileUrl https://*****-oss-ugc-center.oss-cn-beijing.aliyuncs.com/hangtest/pkxkj22x902jILSIO28shxca/%E7%AC%AC%E4%B8%80%E6%89%B9%E6%B5%8B%E8%AF%95/%E9%9F%B3%E9%A2%91%E4%B8%8B%E8%BD%BD/29.wav \
    --FileContent data:audio/ogg;base64,***********AAAAAAABmd9OQAAAAAIw+rFc*E09wdXNIZWFkAQE4AYC7AAAAAABP*2dTAAAAAAAAAAAAAGZ305ABAAAAq*Qr7AE0T3B1c1*****MAAAATGF2Zj*xLjEuMTAwAQAAABQAAABlbmNvZGVyPUxhdmY2MS4xLjEwME9nZ1MAALi8AAAAAAAAZnfTkAIAAA****mJM/p4/z18grqUn5yPhHx8fHuroIyUeoaEfHZ+enBqe3Rv6Y+Yn6anoaKgnJ2gp6W4vLK1p/h8y4MKKi3dNOfMgUB7Lsj55H48QFSAw3SI6PmUZckCcr9DmSvn/vc0P6fPz+592+PYeso42/Ve/u/f1Ud5AjFBLeEdFWNCDTaZZB81V79iVeLQWjh8FATfl+bfil63B5XpjOHo4Y9yxMJNtVeXsGfJKJ7/L3Rqpq79MDHSrI7HkBhmTCbH5nmA6WqyQ/U1u9EBogYiWplc0benvk4SNmcIdjoIaj+N3vZeLgN1+bGA/Ey8MezddrhQ/dzDRVvR4/5PNgFc+e/juPI75hDMfPvni68m8K6NHkJ7hiZgbRlX6sZltYCiSmZvQwVAPodLhK4cVAp11vUVUID4WpTOM6neIt/51+K2o3U+Zfr/W9agRMA7MKlUMQPMC8e+/WW7wDKY8I2/5embjznAZcholRvYR3sZcqpGKErAgWofF9gkzRofJVjefYkIvEmmkc6zfDXi2VBAMSextq9Fj2jBIc7LUI68Hs9A3mD9Rg+SZNLwqlT4cwODl3H3bgqRuNvPKlWesdCA522UUTJQcO7qd0rodCWjzRq2mS00t8Or/Ojk31ZWQzf9g1ooUoaiJ64bgMb8imZrtgGHyEFrkQo+ITubEk5XJFrZ5/2sGgsx9qwesypiKAHfMHPWeWAwaAaPK6v3J0us4bmMkbUugirwXKKbP2Lm+mp/Y1tOmRrTra4fzlhpqipjkz1YAXY8XxgALr8CvSFIIxKqmz2GYiI5rPesyEW1XdkAABTaZyMysPqpgvFMADs0wV/msnZSlEsEmWqRV0QPrq7RI3J58DQqtCC5fw7nE5qeAIBVsM6IrDSxhTjH2S88VRBXbxwOTkUhLbQ51CONCG+W7xZ4e/NtWUVt1Jul4/COw4YNc9Cat4c++4psHeMsi8ncd2ogpBmE9YaZ2Eas8De2fxQAd2Vz+GvNv5CjJwTOd3HlZi6QdJYgiFIKMwomKZsWm8imab9rlwJPzHIUHOiv+S8XHRrFHlAb/7LHgBj6KVJ67zaBUlD0oDsrXyaWlffi9/pZ7D7IPhmOD6aUUnRr2cbW0SZYZImpTfbZUOv7NNoWBp/qrwFZnc5f4WbeRdpmYPicP0CZJsdWrPDpfsZ1h5YRA17uUIA9hdWebJi7V4aepOtjjaexauFBcDGWsJDUncsKSr941OnYuNfYVpO18v9lf4pcSgi9NKd2hOpS+q2zwtZL281Owc2Y+FqfnTCukpVqCDMlSX7NrVvo85jsKfr4y4il6eE5FXxhASBgf5qvWVr4Pgtl94f9gEl3vU5Wc41adbUKksyGx7rVzXbwE9eA//DMhylS/tOfhZESDRMdsAQ+9AK2pGEIYkRJvhD3If5bjR1rFL4QkQzpqPABDgN0lNKFEPPGZ13g7SJFyJzOZJ+R9ohTiij9qM7cgpGRLN35K6YQrCshyac66CO7WC+JQanBRTvbIAn4BWBxV9nUV1V4wDS2W4Tb4Kz5eXYG/NXVPvMJEG02gucAt/FtZNFfwRBLvyKFFRGQ0WH4sXEwrlY+9RL9Ur/iB2kFjugORb92x1Jv2y2Vzp88wnlmfv+VwVk5o/FA170MqQxGUWxZJGv0fTWNoaMHYEoU0Tu1g/mlv/FAeCZyZqu+2VRT6KmSMhZj3HRDoNhpRx/E5MYWI0SLZ/b2DzX45uhQnj/bUY/de8pp497dpJTtPLMkHPf2WHPVnUfBvm7k0kj/0okx+K/g4GtAjSLVQSjKC9iGBuYTqO3****7IzCRGKoMeGjKnYFfu1iNqp \
    --BizType 2_2_3_1410000***
```

Output: 
```
{
    "Response": {
        "Audio": "https://*****-oss-ugc-center.oss-cn-beijing.aliyuncs.com/hangtest/pkxkj22x902jILSIO28shxca/%E7%AC%AC%E4%B8%80%E6%89%B9%E6%B5%8B%E8%AF%95/%E9%9F%B3%E9%A2%91%E4%B8%8B%E8%BD%BD/29.wav",
        "AudioText": "求真务实，充分体现了马克思列宁主义，毛泽东思想，邓小平理论，三个代表重要思想和科学发展观的历史逻辑和内在联系。",
        "CheckDetail": [
            {
                "Desc": "涉政；核心领导",
                "Keywords": [
                    "毛泽东思想"
                ],
                "Label": "Polity",
                "LibName": "",
                "Scene": "",
                "Score": 100,
                "Severity": 0,
                "SeverityDesc": "",
                "SubLabel": "politics_coreleader",
                "Suggest": 2
            }
        ],
        "DataId": "12345***9111",
        "Duration": 12894,
        "FileName": "",
        "Label": "Polity",
        "MediaType": 1,
        "Rate": 100,
        "SubLabel": "politics_coreleader",
        "Suggest": 2,
        "TaskId": "63680997*96*535991",
        "RequestId": "21b7678d-ead6-4d2a-a758-a6f8c8586c6c"
    }
}
```

