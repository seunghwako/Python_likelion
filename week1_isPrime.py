# is_prime 함수는 특정 숫자(n)이 들어왔을 때 
# 그 숫자가 소수면 True를 반환하고 아니면 False를 반환하는 함수입니다.
def is_prime(n):
	if n != 1 : # n이 1일 때 제외
		for i in range(2,n): # 2부터 입력받은 수 까지 반복
			if n % i == 0 : # 입력받은 수로 나누어지면 
				return False # 소수가 아님
	else :
		return False # n이 1일 때

	return True # n이 소수

# prime_number_list 함수는 길이(length)가 들어왔을 때
# 그 길이만큼의 소수를 가지고 있는 리스트를 반환하는 함수입니다.
def prime_number_list(length):
		result = []
		i = 1 # 소수인지 판단하기 위해 1부터 시작하는 변수 선언
		while len(result) != length : # result의 길이와 입력받은 length의 길이가 다르면
			if is_prime(i) == True : # 소수이면
				result.append(i) # result 에 그 숫자 추가
			else : # 소수가 아니면 
				result = result # 그대로 
			i+=1  # 1,2,3,4 계속 올라가면서 판별
		return result # result에 있는 소수들 출력

length = int(input('Length? '))
print(prime_number_list(length))