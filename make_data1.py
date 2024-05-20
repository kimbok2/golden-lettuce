import random
import json
from collections import OrderedDict

# JSON 파일 생성
file = OrderedDict()

N = 20000
max_deposit_id = 38
max_user_id = 10000
unique_pairs = set()

save_dir = './back/goldenlettuce_back/fixtures/deposit_user_data.json'

with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')

    i = 0
    while i < N:
        deposit_id = random.randint(1, max_deposit_id)
        user_id = random.randint(1, max_user_id)
        pair = (deposit_id, user_id)

        if pair not in unique_pairs:
            unique_pairs.add(pair)
            file['model'] = 'finances.depositproduct_join_user'
            file['pk'] = i + 1
            file['fields'] = {
                "depositproduct": deposit_id,
                "user": user_id,
            }

            json.dump(file, f, ensure_ascii=False, indent=4)
            if i != N - 1:
                f.write(',')

            i += 1

    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')