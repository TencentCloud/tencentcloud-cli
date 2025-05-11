**Example 1: 拍照解题请求**



Input: 

```
tccli hunyuan ImageQuestion --cli-unfold-argument  \
    --Model hunyuan-vision-image-question \
    --Messages.0.Role user \
    --Messages.0.Contents.0.Type text \
    --Messages.0.Contents.0.Text 解答图片中的问题 \
    --Messages.0.Contents.1.Type image_url \
    --Messages.0.Contents.1.ImageUrl.Url https://qidian-qbot-1251316161.cos.ap-guangzhou.tencentcos.cn/public/0/0/image/hy/2c4dda9e032a477a6572866de2419ecd9e59076a-6145-46a0-9f47-1048f65cf4f8.png \
    --Stream False
```

Output: 
```
{
    "Response": {
        "RequestId": "b7c3e6e3-a000-4cf1-9201-cdf3dd6352b7",
        "Id": "b7c3e6e3-a000-4cf1-9201-cdf3dd6352b7",
        "Created": 1746614615,
        "Choices": [
            {
                "Index": 0,
                "Message": {
                    "Role": "assistant",
                    "Content": "本题可根据分数、百分数、比的相关性质和运算法则来逐一求解。\n\n### 1. 求解$\\frac{3}{4}\\div(\\space)=\\ 9:(\\space)=\\frac{(\\space)}{20}=(\\space)\\%$\n设$\\frac{3}{4}\\div x = \\frac{3}{20}$，根据“除数$=$被除数$\\div$商”可得$x = \\frac{3}{4}\\div\\frac{3}{20}=\\frac{3}{4}\\times\\frac{20}{3}= 5$；\n设$9:y = \\frac{3}{20}$，根据“后项$=$前项$\\div$比值”可得$y = 9\\div\\frac{3}{20}=9\\times\\frac{20}{3}= 60$；\n将$\\frac{3}{20}$化为百分数，$\\frac{3}{20}=3\\div20 = 0.15 = 15\\%$。\n所以括号内应依次填入$5$、$60$、$15$。\n\n### 2. 求甲数是乙数的百分之几以及乙数比甲数少百分之几\n- 甲、乙两数的比是$5:4$，把甲数看成$5$份，乙数看成$4$份。\n甲数是乙数的：$5\\div4\\times100\\% = 125\\%$；\n乙数比甲数少：$(5 - 4)\\div5\\times100\\% = 1\\div5\\times100\\% = 20\\%$。\n\n### 3. 求括号里的数使等式成立\n根据“一个加数$=$和$-$另一个加数”，可得$\\frac{1}{4}+x = 1$，则$x = 1 - \\frac{1}{4}=\\frac{3}{4}$；\n根据“一个因数$=$积$\\div$另一个因数”，可得$\\frac{2}{5}\\times x = 1$，则$x = 1\\div\\frac{2}{5}=1\\times\\frac{5}{2}=\\frac{5}{2}$；\n根据“除数$=$被除数$\\div$商”，可得$\\frac{6}{11}\\div x = 1$，则$x = \\frac{6}{11}\\div1=\\frac{6}{11}$。\n所以括号内应依次填入$\\frac{3}{4}$、$\\frac{5}{2}$、$\\frac{6}{11}$。\n\n### 4. 求比$50$米少$20\\%$的长度以及$35$米比多少米多$40\\%$\n- 比$50$米少$20\\%$，即$50$米的$(1 - 20\\%)$，$50\\times(1 - 20\\%) = 50\\times0.8 = 40$（米）；\n- 设$35$米比$x$米多$40\\%$，则可列方程$(1 + 40\\%)x = 35$，即$1.4x = 35$，解得$x = 35\\div1.4 = 25$（米）。\n所以括号内应依次填入$40$、$25$。\n\n### 5. 比较大小\n- 计算$\\frac{5}{8}\\div\\frac{4}{5}=\\frac{5}{8}\\times\\frac{5}{4}$，因为$\\frac{5}{4}\\gt\\frac{4}{5}$，所以$\\frac{5}{8}\\times\\frac{5}{4}\\gt\\frac{5}{8}\\times\\frac{4}{5}$，即$\\frac{5}{8}\\div\\frac{4}{5}\\gt\\frac{5}{8}\\times\\frac{4}{5}$；\n- 根据乘法结合律$(a\\times b)\\times c = a\\times(b\\times c)$，可得$(\\frac{1}{2}\\times\\frac{1}{3})\\times\\frac{1}{5}=\\frac{1}{2}\\times\\frac{1}{3}\\times\\frac{1}{5}$；\n- 计算$\\frac{6}{7}\\div\\frac{4}{3}=\\frac{6}{7}\\times\\frac{3}{4}$，因为$\\frac{4}{3}\\gt\\frac{3}{4}$，所以$\\frac{6}{7}\\times\\frac{4}{3}\\gt\\frac{6}{7}\\times\\frac{3}{4}$，即$\\frac{6}{7}\\times\\frac{4}{3}\\gt\\frac{6}{7}\\div\\frac{4}{3}$。\n所以括号内应依次填入$\\gt$、$=$、$\\gt$。\n\n### 6. 求没成活的棵数\n已知果园今年栽果树$200$棵，成活率是$98\\%$，则没成活的占$(1 - 98\\%)$，没成活的棵数为$200\\times(1 - 98\\%) = 200\\times0.02 = 4$（棵）。\n\n综上，答案依次为：\n1. $5$、$60$、$15$；\n2. $125$、$20$；\n3. $\\frac{3}{4}$、$\\frac{5}{2}$、$\\frac{6}{11}$；\n4. $40$、$25$；\n5. $\\gt$、$=$、$\\gt$；\n6. $4$。"
                },
                "FinishReason": "stop"
            }
        ],
        "Usage": {
            "PromptTokens": 1010,
            "CompletionTokens": 836705,
            "TotalTokens": 837715
        },
        "Note": "以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记"
    }
}
```

