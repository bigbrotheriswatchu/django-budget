"""
>>> from django.test import Client
>>> c = Client()

>>> from budget.categories.models import Category
>>> cat = Category.objects.create(name='Misc', slug='misc')

>>> r = c.get('/budget/transaction/')
>>> r.status_code # /budget/transaction/
200
>>> r.context[-1]['transactions']
[]

>>> r = c.get('/budget/transaction/add/')
>>> r.status_code # /budget/transaction/add/
200
>>> type(r.context[-1]['form'])
<class 'budget.transactions.forms.TransactionForm'>

>>> r = c.post('/budget/transaction/add/', {'transaction_type': 'credit', 'name': 'Paycheck', 'amount': '300.00', 'date': '2008-10-14'})
>>> r.status_code # /budget/transaction/add/
302
>>> r['Location']
'http://testserver/budget/transaction/'

>>> r = c.get('/budget/transaction/')
>>> r.status_code # /budget/transaction/
200
>>> r.context[-1]['transactions']
[<Transaction: Paycheck (Credit) - 300>]

>>> r = c.get('/budget/transaction/edit/1/')
>>> r.status_code # /budget/transaction/edit/1/
200
>>> type(r.context[-1]['form'])
<class 'budget.transactions.forms.TransactionForm'>
>>> r.context[-1]['transaction']
<Transaction: Paycheck (Credit) - 300>

>>> r = c.post('/budget/transaction/edit/1/', {'transaction_type': 'credit', 'name': 'My Paycheck', 'amount': '300.00', 'date': '2008-10-14'})
>>> r.status_code # /budget/transaction/edit/1/
302
>>> r['Location']
'http://testserver/budget/transaction/'

>>> r = c.get('/budget/transaction/')
>>> r.status_code # /budget/transaction/
200
>>> r.context[-1]['transactions']
[<Transaction: My Paycheck (Credit) - 300>]

>>> r = c.get('/budget/transaction/delete/1/')
>>> r.status_code # /budget/transaction/delete/1/
200
>>> r.context[-1]['transaction']
<Transaction: My Paycheck (Credit) - 300>

>>> r = c.post('/budget/transaction/delete/1/', {'confirmed': 'Yes'})
>>> r.status_code # /budget/transaction/delete/1/
302
>>> r['Location']
'http://testserver/budget/transaction/'

>>> r = c.get('/budget/transaction/')
>>> r.status_code # /budget/transaction/
200
>>> r.context[-1]['transactions']
[]
"""
