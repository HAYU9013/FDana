import json
import requests

max_step = 20
target = "sportcar2"

def send_request(data):
    # 3. 設定 API 的 URL 與 headers
    url = 'http://127.0.0.1:8188/prompt'
    headers = {'Content-Type': 'application/json'}

    # 4. 發送 POST request 並傳送修改後的 JSON 資料
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 5. 輸出回應結果
    print(response.status_code)
    print(response.json())

def set_step(data, step):
    original_step = step
    addnoise_step = step - 1
    data["prompt"]["4"]["inputs"]["denoise"] = 1-(original_step+1)/max_step
    data["prompt"]["10"]["inputs"]["denoise"] = 1-(addnoise_step)/max_step
    data["prompt"]["21"]["inputs"]["start_at_step"] = addnoise_step
    data["prompt"]["21"]["inputs"]["end_at_step"] = addnoise_step+1
    data["prompt"]["25"]["inputs"]["start_at_step"] = original_step
    data["prompt"]["25"]["inputs"]["end_at_step"] = original_step+1
    data["prompt"]["26"]["inputs"]["start_at_step"] = original_step
    data["prompt"]["26"]["inputs"]["end_at_step"] = original_step+1

    return data

def set_target(data):
    assert isinstance(target, str), "Target must be a string"
    data["prompt"]["6"]["inputs"]["image"] = target+".png"
    data["prompt"]["27"]["inputs"]["filename_prefix"] = target+"_original"
    data["prompt"]["28"]["inputs"]["filename_prefix"] = target+"_addnoise"
    data["prompt"]["33"]["inputs"]["filename_prefix"] = "latents/"+target+"_original"
    data["prompt"]["34"]["inputs"]["filename_prefix"] = "latents/"+target+"_addnoise"

    return data

def __main__():
    # 1. 讀取 JSON 檔案
    with open('one step with latent save.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = set_target(data)
    for i in range(1, max_step-1):

        data = set_step(data, i)
        send_request(data)
        print("Step", i, "done")
__main__()