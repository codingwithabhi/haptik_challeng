void function(int n)
{
int i = 1, s =1;
while (s <= n)
{
i++;
s += i;
n += 1;
n /= 1;
printf("*");
}
}



Answer:

    Program has Time Complexity of O(root(n))