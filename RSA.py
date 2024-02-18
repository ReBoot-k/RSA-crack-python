

class RSA:
    def __init__(self, E=None, N=None, D=None, P=None, Q=None, PHI=None):
        self.set_options(E, N, D, P, Q, PHI)
        self._calibrate()


    def _get_factorize(self, number):
        divisors = []
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                divisors.append((i, number // i))
        return divisors

    def _get_calculate_D(self):
        D = 0
        while D * self.E % self.PHI != 1:
            D += 1
        return D

    def _calibrate(self):
        if not self.E:
            print("[X] E (открытый ключ) отсутствует")
            exit(1)

        if self.PHI and (self.P and (not self.Q)):
            self.Q = self.PHI // (self.P - 1) + 1

        if self.PHI and (self.Q and (not self.P)):
            self.P = self.PHI // (self.Q - 1) + 1

        if self.N and (not self.P or not self.Q):
            found = False
            divisors = self._get_factorize(self.N)
            if not (self.P and self.Q):
                self.P, self.Q = divisors[0]
                found = True
            else:
                for divisor in divisors:
                    if self.P in divisor or self.Q in divisor:
                        self.P, self.Q = divisor
                        found = True
            if not found:
                print(f"[X] Не удалось найти подходящие делители для N")
                exit(1)
                

        if not self.N:
            self.N = self.P * self.Q

        if not self.PHI:
            self.PHI = (self.P - 1) * (self.Q - 1)
        if not self.D:
            self.D = self._get_calculate_D()


    def set_options(self, E=None, N=None, D=None, P=None, Q=None, PHI=None):
        self.E = E  # открытый ключ
        self.N = N  # модуль
        self.D = D  # закрытый ключ
        self.P = P  # первый простой множитель
        self.Q = Q  # второй простой множитель
        self.PHI = PHI  # функция Эйлера

    def get_decrypt_message(self, encrypt):
        decrypted_chars = [chr(i ** self.D % self.N) for i in encrypt]
        return "".join(decrypted_chars)



