git add -A
if "%1" equ "" git commit -m "Update."
if "%1" neq "" git commit -m "%1"
git push