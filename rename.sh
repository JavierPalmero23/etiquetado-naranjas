a=1
for i in *.jpg; do
  new="Original$(printf "%04d" $a).png"
  mv -i -- "$i" "$new"
  let a=a+1
done
