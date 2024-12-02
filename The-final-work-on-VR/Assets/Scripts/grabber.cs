using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class grabber : MonoBehaviour
{
    private GameObject armBody;
    private GameObject armPart1;
    private GameObject bar4;

    // Start is called before the first frame update
    void Start()
    {
        armBody = GameObject.Find("ArmBody");
        armPart1 = GameObject.Find("ArmPart1");
        bar4 = GameObject.Find("Bar4");

        Invoke("grab", 4);
        Invoke("teleportBrick", 4.3f);
    }

    private void teleportBrick()
    {
        armBody.transform.Rotate(new Vector3(0, 0, 96));
        armPart1.transform.Rotate(new Vector3(0, 45, 0));

        bar4.transform.position = new Vector3(1, 5.7f, 14);
        bar4.transform.Rotate(new Vector3(180, 0, 0));
    }

    private void grab()
    {
        armBody.transform.Rotate(new Vector3(0, 0, -86));
        armPart1.transform.Rotate(new Vector3(0, -45, 0));


    }

    // Update is called once per frame
    void Update()
    {

    }
}
