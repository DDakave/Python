sports1 ={"Ram","Raj","Dev","Shweta"}

sports2 = {"shweta","Raj","Hiral","Arjun","Ram"}

#to find out total participents in the sports

total_count = sports1|sports2

print("Total Participents:",total_count)

#for s in total_countprint(s)

#set Difference

new_sports1 = sports1-sports2

print("the new sports one list is:",new_sports1)




email_id = ["abc@gmail.com","pqr@gmail.com","stq@gmail.com","ncrd@gmail.com","pqr@gmail.com","abc@gmail.com","drdi@gmail.com","stq@gmail.com"]
print("The data of email as below:")
print(email_id)

unique_emails = set(email_id)
print(unique_emails)

new_emails={"raj@gmail.com","abc@gmail.com","pqr@gmail.com","sahil@gmail.com"}
update = new_emails-unique_emails
print("new customers are:",update)
