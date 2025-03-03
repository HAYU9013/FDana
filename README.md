## 使用步驟 
> (大概拉，大概寫寫而已，有問題再問我)
1. 開啟 comfy ui
   - 在 comfy ui 目錄下開啟 cmd
   - `conda activate comfy`
   - `python main.py`
2. 把要用的圖片(.png) 放到 comfyui/input
2. 用 /generate.py
   - 改 target 成你的檔案名稱
   - 執行
   - 等待
3. 在 /analyiz 的 python note book
   - 前兩個 block 會把檔案整理起來
   - 到 Comfy ui 資料夾找到 hspace 和 latent 中 叫 photo 的資料夾
   - 改名並放到 /analyiz 中對應的資料夾
   - 在 targets 的 list 中加上你改過的名字
   - 執行程式到出現兩張圖表為止
   - 後面是爛掉的 code 別理他
