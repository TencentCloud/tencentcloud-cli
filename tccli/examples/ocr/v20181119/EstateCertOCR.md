**Example 1: 不动产权证识别示例代码**



Input: 

```
tccli ocr EstateCertOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "Obligee": "周框吉",
        "Ownership": "单独所有",
        "Location": "番禺区南村镇沙溪大道520号",
        "Unit": "440113013008G800003F00230055",
        "Type": "国有建设用地使用权/房屋(构筑物)所有权",
        "Property": "土地:出让/房屋:商品房",
        "Usage": "土地:/房屋:住宅",
        "Area": "270.13平方米",
        "Term": "2017年03月01日-2087年03月01日",
        "Angle": 0,
        "Other": "",
        "Number": "07037799",
        "RequestId": "ac3643f3-0898-4449-9999-f1c1aa98939c"
    }
}
```

