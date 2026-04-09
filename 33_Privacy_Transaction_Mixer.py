import random

class TxMixer:
    def mix(self, inputs, outputs):
        shuffled = inputs.copy()
        random.shuffle(shuffled)
        return {"shuffled_inputs":shuffled,"outputs":outputs}

if __name__ == "__main__":
    mixer = TxMixer()
    res = mixer.mix(["a","b","c"],["x","y","z"])
    print(f"混合结果:{res}")
