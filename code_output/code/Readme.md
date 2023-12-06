<!--
 * @Author: Zheng Wang zwang3478@gatech.edu
 * @Date: 2023-11-29 15:33:58
 * @LastEditors: Zheng Wang zwang3478@gatech.edu
 * @LastEditTime: 2023-12-04 15:48:15
 * @FilePath: /final_project/dist/Readme.md
-->
1. The 'DATA' directory should be put into the same directory as the code and result file.
2. The executable file is created by using ```pyinstaller``` to convert python files to executabel file.
3. There are four available input parameters, which is describe as follows: \
```-inst```: instance name or city name, which should be selected from [Roanoke, NYC, UKansasState, Champaign, Berlin, UMissouri, Boston, Atlanta, Cincinnati, Denver, SanFrancisco, Toronto, Philadelphia]  \
```-alg```: the name of algorithm, which should be selected from [BF, Approc, LS, hill_climbing] \
```-time```: the cutoff time for algorithm except for Approx. The default value is set to 50 \
```-seed```: the random seed for Approx, LS algorithms. The default value if 42.


 
