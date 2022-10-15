
var name = prompt("what is name buddy? ")
user.innerHTML = name;

const rock = document.querySelector('.rock');
const paper = document.querySelector('.paper')
const seizer = document.querySelector('.seizer');
const winner = document.querySelector('.winner')
const user = document.querySelector("name")

document.addEventListener('click' , ()=>{
    


})



function sps( t)
{
    var comp;
    if (t < 3)
    {
        comp = 'r';
    }
    else if (t > 3 && t < 6)
    {
        comp = 'p';
    }
    else
    {
        comp = 's';
    }
    return comp;
}
function winner( you,  comp)
{
    if (you == comp)
    {
        return 0;
    }
    else if (you == 's' && comp == 'r')
    {
        return -1;
    }
    else if (you == 's' && comp == 'p')
    {

        return 1;
    }
    else if (you == 'p' && comp == 'r')
    {

        return 1;
    }
    else if (you == 'p' && comp == 's')
    {

        return -1;
    }
    else if (you == 'r' && comp == 'p')
    {
        return -1;
    }
    else if (you == 'r' && comp == 's')
    {
        return 1;
    }
}
function answer(x)
{
    if (x == 0)
    {
        cout << "game draw !" << endl;
    }
    else if (x == 1)
    {
        cout << "you won !" << endl;
    }
    else
    {
        cout << "you lose !" << endl;
    }
}
function main()
{
    var u= 100;
    while (u--)
    {
        
    cout << "please enter 'r' for rock , 'p' for paper and 's' for seizer : ";
    let you, comp;
    cin >> you;
    srand(time(0));
    let number = rand() % 10 + 1;
    comp = sps(number);
    let result = winner(you, comp);
    // int t = rand(100);
    cout << "you chose " << you << " and the computer chose " << comp << " , hence" << endl;
    answer(result);
    // cout<<you<<" "<<comp;
    }
    

    return 0;
}
