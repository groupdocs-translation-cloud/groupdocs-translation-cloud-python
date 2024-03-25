rmdir /S /Q build
rmdir /S /Q dist 
python setup.py bdist_wheel
python -m twine upload --repository pypi dist/* -u groupdocscloud -p 4!5].q83Wc:n.WU