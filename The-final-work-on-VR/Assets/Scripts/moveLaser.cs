using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using Unity.VisualScripting;
using UnityEngine;

public class move_laser : MonoBehaviour
{
    private GameObject Mech;
    private GameObject Laser;
    public Collider button;
    public int side1 = 1;
    public int side2 = 1;

    private bool move1 = true;

    private void Awake()
    {
        Mech = GameObject.Find("Mechanism");
        Laser = GameObject.Find("Lazer");
        Invoke("changeBrick", 13);
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.G))
        {
            Vector3 newPosition = Mech.transform.localPosition + new Vector3(0, 0, side1 * 0.25f);
            Mech.transform.localPosition = newPosition;
            //Debug.Log(Mech.transform.position.z);
            //Debug.Log(Mech.transform.position.z < -10);
            if (Mech.transform.localPosition.z < -10)
            {
                Mech.transform.localPosition = new Vector3(-7.39f, 1.77f, -10);
            }
            if (Mech.transform.localPosition.z > 0)
            {
                Mech.transform.localPosition = new Vector3(-7.39f, 1.77f, 0);
            }
        }

        Invoke("changeMove", 6);

        if (move1)
        {
            Invoke("move", 5.5f);
        }
        Invoke("move2", 13);

        //if (button.bounds.Contains(Camera.main.transform.position))
        //{

        //}
    }

    private void changeMove()
    {
        move1 = false;
    }
    private void move()
    {
        moveToX(-0.1f);
        moveToZ(-8.7f);
    }
    private void changeBrick()
    {

        GameObject prefab = GameObject.Find("Bar1 (3)");
        GameObject originalBar = GameObject.Find("Bar4");

        GameObject bar1 = Instantiate(
            prefab,
            new Vector3(originalBar.transform.position.x, originalBar.transform.position.y, originalBar.transform.position.z),
            Quaternion.identity
            );
        GameObject bar2 = Instantiate(
            prefab,
            new Vector3(originalBar.transform.position.x + 0.5f, originalBar.transform.position.y, originalBar.transform.position.z),
            Quaternion.identity
            );
        GameObject bar3 = Instantiate(
            prefab,
            new Vector3(originalBar.transform.position.x - 0.5f, originalBar.transform.position.y, originalBar.transform.position.z),
            Quaternion.identity
            );
        Destroy(originalBar);
    }

    private void move2()
    {
        Vector3 newPosition = Mech.transform.localPosition + new Vector3(0, 0, 0.02f);
        Mech.transform.localPosition = newPosition;
        if (Mech.transform.localPosition.z > 0)
        {
            Mech.transform.localPosition = new Vector3(-7.39f, 1.77f, 0);
        }
    }

    private void moveToZ(float coordZ)
    {
        Vector3 newPosition = Mech.transform.localPosition + new Vector3(0, 0, -0.01f);
        Mech.transform.localPosition = newPosition;
        if (Mech.transform.localPosition.z < coordZ)
        {
            Mech.transform.localPosition = new Vector3(-7.39f, 1.77f, coordZ);
        }
    }
    private void moveToX(float coordX)
    {
        Vector3 newPosition = Laser.transform.localPosition + new Vector3(-0.0002f, 0, 0);
        Laser.transform.localPosition = newPosition;
        if (Laser.transform.localPosition.x < coordX)
        {
            Laser.transform.localPosition = new Vector3(coordX, Laser.transform.localPosition.y, Laser.transform.localPosition.z);
        }
    }

    //private void MoveObjects()
    //{

    //    foreach (GameObject obj in objectsToMove)
    //    {
    //        Vector3 newPosition = obj.transform.position + new Vector3(0.05f, 0, 0);
    //        obj.transform.position = newPosition;
    //    }
    //}
}
