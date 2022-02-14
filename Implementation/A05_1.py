
# 문제점: 현재 상태를 list에 append로 저장을 해서 search하는데 시간이 걸림

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        if build[3] == 0:
            if remove_func(build, answer):
                answer.remove(build[0:3])
        else:
            if build_func(build, answer):
                answer.append(build[0:3])
    answer = sorted(answer)

    return answer


def build_func(build, answer):
    # x,y에 건축물이 있는지 실패
    if build[2] == 0:  # 기둥
        if build[1] == 0:  # 땅
            return True
        if [build[0], build[1], 1] in answer:
            return True
        if [build[0], build[1] - 1, 0] in answer:
            return True
        if [build[0] - 1, build[1], 1] in answer:
            return True
        return False
    else:  # 보
        if [build[0], build[1] - 1, 0] in answer:
            return True
        if [build[0] + 1, build[1] - 1, 0] in answer:
            return True
        if [build[0] - 1, build[1], 1] in answer:
            if [build[0] + 1, build[1], 1] in answer:
                return True
        return False


def remove_func(build, answer):
    if build[2] == 0:  # 기둥
        if [build[0], build[1] + 1, 0] in answer:
            if not ([build[0] - 1, build[1] + 1, 1] in answer or [build[0], build[1] + 1, 1] in answer):
                return False
        if [build[0] - 1, build[1] + 1, 1] in answer:
            if not [build[0] - 1, build[1], 0] in answer:
                if not ([build[0] - 2, build[1] + 1, 1] in answer and [build[0], build[1] + 1, 1] in answer):
                    return False
        if [build[0], build[1] + 1, 1] in answer:
            if not [build[0] + 1, build[1], 0] in answer:
                if not ([build[0] - 1, build[1] + 1, 1] in answer and [build[0] + 1, build[1] + 1, 1] in answer):
                    return False
        return True
    else:  # 보
        if [build[0] - 1, build[1], 1] in answer:
            if not ([build[0], build[1] - 1, 0] in answer or [build[0] - 1, build[1] - 1, 0] in answer):
                return False
        if [build[0] + 1, build[1], 1] in answer:
            if not ([build[0] + 2, build[1] - 1, 0] in answer or [build[0] + 1, build[1] - 1, 0] in answer):
                return False
        if [build[0], build[1], 0] in answer:
            if not ([build[0] - 1, build[1], 1] in answer or [build[0], build[1] - 1, 0] in answer):
                return False
        if [build[0] + 1, build[1], 0] in answer:
            if not ([build[0] + 1, build[1] - 1, 0] in answer or [build[0] + 1, build[1], 1] in answer):
                return False
        return True