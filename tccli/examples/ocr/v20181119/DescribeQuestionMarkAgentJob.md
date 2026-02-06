**Example 1: 成功示例**



Input: 

```
tccli ocr DescribeQuestionMarkAgentJob --cli-unfold-argument  \
    --JobId 1410888033157898240
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "ErrorCode": "",
        "ErrorMessage": "",
        "JobStatus": "DONE",
        "MarkInfos": [
            {
                "AnswerInfos": [],
                "MarkInfos": [
                    {
                        "AnswerInfos": [
                            {
                                "AnswerAnalysis": "首先将除法转化为乘法，对分子分母因式分解后约分，正确计算过程为$\\frac{2}{a-1}\\div\\frac{2a-4}{a^2-1}=\\frac{2}{a-1}\times\\frac{(a+1)(a-1)}{2(a-2)}=\\frac{a+1}{a-2}$，手写答案最后一步分母错误。",
                                "HandwriteInfo": "$\\frac{2}{a-1}\\div\\frac{2a-4}{a^2-1}=\\frac{2}{a-1}\times\\frac{(a+1)(a-1)}{2(a-2)}=\\frac{a+1}{a+2}$",
                                "HandwriteInfoPositions": [
                                    113,
                                    648,
                                    558,
                                    648,
                                    558,
                                    698,
                                    113,
                                    698
                                ],
                                "IsCorrect": false,
                                "KnowledgePoints": [],
                                "RightAnswer": ""
                            }
                        ],
                        "MarkInfos": [],
                        "MarkItemTitle": "(1)小琪猜测,墨水遮住的内容是“2a”,请你根据小琪的猜测完成计算;"
                    },
                    {
                        "AnswerInfos": [
                            {
                                "AnswerAnalysis": "设被墨水遮住的部分为A，根据题意$\\frac{2}{a-1}\\div\\frac{A-4}{a^2-1}=\\frac{1}{a-2}$，先将除法转化为乘法，得到$\\frac{2}{a-1}\times\\frac{(a+1)(a-1)}{A-4}=\\frac{1}{a-2}$，化简后求解A，正确过程为：$\\frac{2(a+1)}{A-4}=\\frac{1}{a-2}$，交叉相乘得$A-4=2(a+1)(a-2)=2(a^2-a-2)=2a^2-2a-4$，所以$A=2a^2-2a$，手写答案计算错误，没有正确求出被遮住的二次二项式。",
                                "HandwriteInfo": "$\\frac{2}{a-1}\\div\\frac{1}{a-2}=\\frac{2(a-2)}{a-1}=\\frac{2(a-2)(a+1)}{a^2-1}=\\frac{2a^2-2a-2}{a^2-1}$",
                                "HandwriteInfoPositions": [
                                    164,
                                    698,
                                    450,
                                    698,
                                    450,
                                    855,
                                    164,
                                    855
                                ],
                                "IsCorrect": false,
                                "KnowledgePoints": [],
                                "RightAnswer": ""
                            }
                        ],
                        "MarkInfos": [],
                        "MarkItemTitle": "(2)第二天,小琪的同桌告诉她,这道题被墨水遮住的是一个二次二项式,并且这道题的标准答案是$\\frac{1}{a-2}$,请你通过计算说明墨水遮住的内容是什么."
                    }
                ],
                "MarkItemTitle": "1. 小琪在做作业时发现有一道题的一部分被墨水遮住了,如图所示。计算: $\\frac{2}{a-1}\\div\\frac{▄-4}{a^2-1}$."
            },
            {
                "AnswerInfos": [],
                "MarkInfos": [
                    {
                        "AnswerInfos": [
                            {
                                "AnswerAnalysis": "先根据垂直的性质得到∠A=∠B=90°，再结合运动速度和时间算出AP、BQ、BP的长度，得到BP=AC，然后利用SAS证明△ACP≅△BPQ，最后利用全等三角形的性质和直角三角形的两个锐角互余，推出∠CPQ=90°，从而得到PC⊥PQ。",
                                "HandwriteInfo": "全等，PC⊥PQ。∵AC⊥AB，BD⊥AB ∴∠A=∠B=90°。∵AP=BQ=2 ∴BP=5 ∴BP=AC。在△ACP和△BPQ中，{AP=BQ，∠A=∠B，AC=BP ∴△ACP≅△BPQ(SAS)。∴∠C=∠BPQ。∵∠C+∠APC=90° ∴∠BPQ+∠APC=90°。∴PC⊥PQ。",
                                "HandwriteInfoPositions": [
                                    595,
                                    440,
                                    905,
                                    440,
                                    905,
                                    847,
                                    595,
                                    847
                                ],
                                "IsCorrect": true,
                                "KnowledgePoints": [],
                                "RightAnswer": ""
                            }
                        ],
                        "MarkInfos": [],
                        "MarkItemTitle": "(1)若点Q的运动速度与点P的运动速度相等,当t=1时,判断△ACP与△BPQ是否全等,并判断此时线段PC和线段PQ的位置关系,请分别说明理由."
                    },
                    {
                        "AnswerInfos": [
                            {
                                "AnswerAnalysis": "本题需要分两种情况讨论△ACP与△BPQ全等的情况：情况一：△ACP≅△BPQ，此时AC=BP，AP=BQ；情况二：△ACP≅△BQP，此时AC=BQ，AP=BP。学生只考虑了其中一种情况，答案不完整。",
                                "HandwriteInfo": "若△ACP≅△BPA，则AC=BP，AP=BQ，即{5=7-2t，2t=xt，解得{x=2，t=1。当x=2时，△ACP与△BPQ全等。",
                                "HandwriteInfoPositions": [
                                    595,
                                    440,
                                    905,
                                    440,
                                    905,
                                    847,
                                    595,
                                    847
                                ],
                                "IsCorrect": false,
                                "KnowledgePoints": [],
                                "RightAnswer": ""
                            }
                        ],
                        "MarkInfos": [],
                        "MarkItemTitle": "(2)如图②,若将“AC⊥AB,BD⊥AB”改为“∠CAB=∠DBA”,点Q的运动速度为xcm/s,其他条件不变,当x的值为多少时,△ACP与△BPQ全等?"
                    }
                ],
                "MarkItemTitle": "如图①,AB=7cm,AC⊥AB,BD⊥AB,垂足分别为A,B,AC=5cm.点P在线段AB上以2cm/s的速度由点A向点B运动,同时点Q在射线BD上运动,它们运动的时间为ts(当点P运动结束时,点Q运动随之结束)."
            },
            {
                "AnswerInfos": [],
                "MarkInfos": [],
                "MarkItemTitle": "单题跨页题型，完整题目批改内容已经显示在上一题"
            },
            {
                "AnswerInfos": [
                    {
                        "AnswerAnalysis": "通过证明Rt△BOF和Rt△COE全等，得到∠FBO=∠ECO，再结合OB=OC推出∠OBC=∠OCB，进而得到∠ABC=∠ACB，最后根据等角对等边证明AB=AC，整个证明过程逻辑严谨，步骤正确。",
                        "HandwriteInfo": "证:在Rt△BOF和Rt△COE中\n{OF=OE\nOB=OC.\n∴Rt△BOF≅Rt△COE\n∴∠FBO=∠ECO\n∵OB=OC\n∴∠OBC=∠OCB\n∴∠FBO+∠OBC=∠ECO+∠OCB即∠ABC=∠ACB\n∴AB=AC .",
                        "HandwriteInfoPositions": [
                            595,
                            934,
                            1003,
                            934,
                            1003,
                            1282,
                            595,
                            1282
                        ],
                        "IsCorrect": true,
                        "KnowledgePoints": [],
                        "RightAnswer": ""
                    }
                ],
                "MarkInfos": [],
                "MarkItemTitle": "3. 如图，△ABC内部一点O到两边AB,AC所在直线的距离相等，且OB=OC.求证:AB=AC."
            }
        ],
        "RequestId": "5c0fb341-3122-409e-ba5d-12f888397057"
    }
}
```

