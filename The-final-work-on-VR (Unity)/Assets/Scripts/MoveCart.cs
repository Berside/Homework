using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCart : MonoBehaviour
{
    private float currentSpeed = 0;    // 0-1 from no speed to full speed
    private float accel = 0.5f;        // accelerate to full speed in 2 seconds (1 / accel)
    private float speed = 1;        // accelerate to full speed in 2 seconds (1 / accel)
    public float punchZ;
    public float punchX;
    private Rigidbody rb;
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.AddForce(new Vector3(punchX, 0, punchZ));
    }
    void Update()
    {
        //if (Input.GetKeyDown(KeyCode.G))
        //{
        //    rb.AddForce(new Vector3(punchX, 0, punchZ));
        //}
    }
}
