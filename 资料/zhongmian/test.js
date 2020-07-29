function pick(obj, keys) {
  return keys.map(k => k in obj ? {[k]: obj[k]} : {})
        .reduce((res, o) => Object.assign(res, o), {});
}
const row = {
  'accounts.id': 1,
  'client.name': 'John Doe',
  'bank.code': 'MDAKW213'
};
const table = [
  row,
  {'accounts.id': 3, 'client.name': 'Steve Doe', 'bank.code': 'STV12JB'}
];
pick(row, ['client.name']); // 取到了 client name
table.map(row => pick(row, ['client.name'])); // 取到了一系列 client name