
using UnityEngine;
using UnityEngine.UI;

public class CollisionCounter : MonoBehaviour
{
    public int counter = 0;
    public Text counterText;

    void OnCollisionEnter(Collision collision)
    {
        counter--;
        counterText.text = "Collisions: " + counter;
    }
}
